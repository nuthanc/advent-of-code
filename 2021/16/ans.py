from os import path


def read_file():
    THIS_DIR = path.dirname(path.realpath(__file__))
    file_path = path.join(THIS_DIR, 'input.txt')
    with open(file_path) as f:
        return f.read()

def decode_headers(binary, cur):
    if cur + 6 < len(binary):
        packet_version = int(binary[cur:cur+3], 2)
        cur += 3
        packet_id = int(binary[cur:cur+3], 2) 
        cur += 3
        return packet_version, packet_id, cur
    return None,None,None

def first(binary, cur):
    version_sum = 0
    if cur < len(binary):
        packet_version, packet_id, cur = decode_headers(binary, cur)
        if packet_version == None and packet_id == None:
            return version_sum, cur
        version_sum += packet_version
        # print(packet_version, packet_id)
        if packet_id == 4:
            literal_val = ""
            for i in range(cur, len(binary), 5):
                literal_val += binary[i+1:i+5]
                if binary[i] == '0':
                    cur = i + 5
                    break
            # print(int(literal_val, 2))
        else:
            length_type_id = binary[cur]
            cur += 1
            if length_type_id == '0':
                total_len = int(binary[cur:cur+15], 2)
                cur += 15
                subpackets_len = cur + total_len
                while cur < subpackets_len: 
                    # first(binary, cur, version_sum, subpackets_len, float('inf'))
                    vsum, cur_ptr = first(binary, cur)
                    version_sum += vsum
                    cur = cur_ptr
            else:
                num_subpackets = int(binary[cur:cur+11], 2)
                cur += 11
                while num_subpackets > 0:
                    num_subpackets -= 1
                # first(binary, cur, version_sum, float('inf'), num_subpackets)
                    vsum, cur_ptr = first(binary, cur)
                    version_sum += vsum
                    cur = cur_ptr
    return version_sum, cur
        # print(version_sum)
                
def solution():
    hex_string = read_file()
    num_0f_bits = len(hex_string) * 4
    binary = bin(int(hex_string, 16))[2:].zfill(num_0f_bits)
    # print(binary)
    print(first(binary, 0)[0])

solution()