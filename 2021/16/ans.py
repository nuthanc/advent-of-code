'''
Step 1: Verify the Constraints

* Input is hexadecimal number

Step 2: Write down some test cases

* 9C0141080250320F1802104A08
Packet id: 7
Packet id: 0
Current value:  1
Values:  [inf]
Operators:  [7, 0]

Current value:  3
Values:  [1]
Operators:  [7, 0]

Packet id: 1
Current value:  2
Values:  [4, inf]
Operators:  [7, 1]

Current value:  2
Values:  [4, 2]
Operators:  [7, 1]

Current value:  16
Values:  [inf]
Operators:  [7]

16
* Test cases where there is delay in processing of sub-packets due to the presence of another operator immediately
* Test cases where there isn't any delay in processing of sub-packets
    * Is there a correlation between operator index and value index?
'''
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
            print(int(literal_val, 2))
        else:
            length_type_id = binary[cur]
            cur += 1
            if length_type_id == '0':
                total_len = int(binary[cur:cur+15], 2)
                cur += 15
                subpackets_len = cur + total_len
                while cur < subpackets_len: 
                    vsum, cur_ptr = first(binary, cur)
                    version_sum += vsum
                    cur = cur_ptr
            else:
                num_subpackets = int(binary[cur:cur+11], 2)
                cur += 11
                while num_subpackets > 0:
                    num_subpackets -= 1
                    vsum, cur_ptr = first(binary, cur)
                    version_sum += vsum
                    cur = cur_ptr
    return version_sum, cur
        # print(version_sum)


def perform_operation(parsed_tuple):
    operator_id, packets, _ = parsed_tuple
    if operator_id == 0:
        return sum(map(perform_operation, packets))
    elif operator_id == 1:
        val = 1
        for packet in packets:
            val *= perform_operation(packet)
        return val
    elif operator_id == 2:
        return min(map(perform_operation, packets))
    elif operator_id == 3:
        return max(map(perform_operation, packets))
    elif operator_id == 4:
        return packets
    elif operator_id == 5:
        return 1 if perform_operation(packets[0]) > perform_operation(packets[1]) else 0
    elif operator_id == 6:
        return 1 if perform_operation(packets[0]) < perform_operation(packets[1]) else 0
    elif operator_id == 7:
        return 1 if perform_operation(packets[0]) == perform_operation(packets[1]) else 0

def parse(binary, cur):
    if cur < len(binary):
        _, packet_id, cur = decode_headers(binary, cur)
        # print(packet_version, packet_id)
        if packet_id == 4:
            literal_val = ""
            for i in range(cur, len(binary), 5):
                literal_val += binary[i+1:i+5]
                if binary[i] == '0':
                    cur = i + 5
                    break
            value = int(literal_val, 2)
            return (packet_id, value, cur)
        else:
            # print(f'Packet id: {packet_id}')
            packets = []
            length_type_id = binary[cur]
            cur += 1
            if length_type_id == '0':
                total_len = int(binary[cur:cur+15], 2)
                cur += 15
                subpackets_len = cur + total_len
                while cur < subpackets_len:
                    id, value, cur_ptr = parse(binary, cur)
                    cur = cur_ptr
                    packets.append((id, value, cur))
            else:
                num_subpackets = int(binary[cur:cur+11], 2)
                cur += 11
                while num_subpackets > 0:
                    num_subpackets -= 1
                    id, value, cur_ptr = parse(binary, cur)
                    cur = cur_ptr
                    packets.append((id, value, cur))
            return (packet_id, packets, cur)
                
def solution():
    hex_string = read_file()
    num_of_bits = len(hex_string) * 4
    binary = bin(int(hex_string, 16))[2:].zfill(num_of_bits)
    def second():
        parsed_tuple = parse(binary, 0)
        print(parsed_tuple)
        print(perform_operation(parsed_tuple))
    second()

solution()