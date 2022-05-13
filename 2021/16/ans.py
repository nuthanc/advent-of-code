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


def perform_operation(current_value, operators, values):
    print('Current value: ', current_value)
    print('Values: ', values)
    print('Operators: ', operators, end='\n\n')
    operator_id = operators[-1]
    if values[-1] == float('inf'):
        values.pop()
        values.append(current_value)
    else:
        if operator_id == 0:
            values[-1] += current_value
        elif operator_id == 1:
            values[-1] *= current_value
        elif operator_id == 2:
            previous_value = values.pop()
            values.append(min(current_value, previous_value))
        elif operator_id == 3:
            previous_value = values.pop()
            values.append(max(current_value, previous_value))
        elif operator_id == 5:
            previous_value = values.pop()
            values.append(1 if previous_value > current_value else 0)
            if len(operators):
                operators.pop()
        elif operator_id == 6:
            previous_value = values.pop()
            values.append(1 if previous_value < current_value else 0)
            if len(operators):
                operators.pop()
        elif operator_id == 7:
            previous_value = values.pop()
            values.append(1 if previous_value == current_value else 0)
            if len(operators):
                operators.pop()

def second(binary, cur, operators, values):
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
            current_value = int(literal_val, 2)
            perform_operation(current_value, operators, values)
        else:
            if values[-1] != float('inf'):
                operators.pop()
                values.append(float('inf'))
            operators.append(packet_id)
            print(f'Packet id: {packet_id}')
            length_type_id = binary[cur]
            cur += 1
            if length_type_id == '0':
                total_len = int(binary[cur:cur+15], 2)
                cur += 15
                subpackets_len = cur + total_len
                while cur < subpackets_len:
                    vsum, cur_ptr = second(binary, cur, operators, values)
                    version_sum += vsum
                    cur = cur_ptr
            else:
                num_subpackets = int(binary[cur:cur+11], 2)
                cur += 11
                while num_subpackets > 0:
                    num_subpackets -= 1
                    vsum, cur_ptr = second(binary, cur, operators, values)
                    version_sum += vsum
                    cur = cur_ptr
    return version_sum, cur
                
def solution():
    hex_string = read_file()
    num_of_bits = len(hex_string) * 4
    binary = bin(int(hex_string, 16))[2:].zfill(num_of_bits)
    operators = []
    values = [float('inf')]
    second(binary, 0, operators, values)
    if len(operators):
        operators.pop()
    while len(operators) > 0:
        current_value = values.pop()
        if len(values) == 0:
            values.append(float('inf'))
        perform_operation(current_value, operators, values)
        if len(operators):
            operators.pop()
    print(values[0]) # 843: Too low

solution()