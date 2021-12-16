import numpy as np


def parse_packet_header(bits):
    global version_sum
    if len(bits) < 6:
        return ""
    indx = 0
    pkt_ver = int(bits[indx:indx+3], 2)
    version_sum += pkt_ver
    indx += 3
    pkt_id = int(bits[indx:indx+3], 2)
    indx += 3
    header = [pkt_ver, pkt_id]
    if pkt_id == 4:
        return parse_literal(header, bits[indx:])
    else:
        return parse_operator_header(header, bits[indx:])
       
def parse_literal(header, bits):
    indx = 0
    enc_num = 0
    prefix = int(bits[indx], 2)
    indx +=1
    while prefix == 1:
        sub_num = int(bits[indx:indx+4], 2)
        indx += 4
        enc_num = (enc_num << 4) + sub_num
        prefix = int(bits[indx], 2)
        indx += 1
    sub_num = int(bits[indx:indx+2], 2)
    indx += 4
    enc_num = (enc_num << 4) + sub_num
    packet.append((header, 'LITERAL', enc_num))
    return bits[indx:]

def parse_operator_header(header, bits):
    indx = 0
    type_id = int(bits[indx], 2)
    indx += 1
    if type_id == 0:
        sub_pkt_len = int(bits[indx:indx + 15], 2)
        indx += 15
        packet.append((header, 'OPERATOR_LEN', sub_pkt_len))
        return parse_packet_len(bits[indx:], sub_pkt_len)
    else:
        sub_pkt_num = int(bits[indx:indx+11], 2)
        indx += 11
        packet.append((header, 'OPERATOR_NUM', sub_pkt_num))
        return parse_packet_num(bits[indx:], sub_pkt_num)        

def parse_packet_num(bits, num_pkts):
    for i in range(num_pkts):
        bits = parse_packet_header(bits)
    return bits

def parse_packet_len(bits, num_bits):
    parse_bits = bits[0:num_bits]
    while(len(parse_bits) > 0):
        parse_bits = parse_packet_header(parse_bits)
    return bits[num_bits:]

binary = ""
packet = []
version_sum = 0
with open('input.txt') as file:
    for line in file:
        binary = ""
        for char in line.strip():
            binary += format(int(char, 16), "04b")
        parse_packet_num(binary, 1)
print('Part 1: ' + str(version_sum))


def parse_packet_header_2(bits):
    if len(bits) < 6:
        return [0, ""]
    indx = 0
    global version_sum
    pkt_ver = int(bits[indx:indx+3], 2)
    version_sum += pkt_ver
    indx += 3
    pkt_id = int(bits[indx:indx+3], 2)
    indx += 3
    if pkt_id == 4:
        enc_num = 0.0
        prefix = int(bits[indx], 2)
        indx +=1
        while prefix == 1:
            sub_num = float(int(bits[indx:indx+4], 2))
            indx += 4
            enc_num = (enc_num*16.0) + sub_num
            prefix = int(bits[indx], 2)
            indx += 1
        sub_num = float(int(bits[indx:indx+4], 2))
        indx += 4
        enc_num = (enc_num*16.0) + sub_num
        return [enc_num, bits[indx:]]
    else:
        if pkt_id == 0:
            command = 'SUM'
        elif pkt_id == 1:
            command = 'PRD'
        elif pkt_id == 2:
            command = 'MIN'
        elif pkt_id == 3:
            command = 'MAX'
        elif pkt_id == 5:
            command = 'GRT'
        elif pkt_id == 6:
            command = 'LST'
        elif pkt_id == 7:
            command = 'EQU'
        else:
            print('Something has gone wrong')
        type_id = int(bits[indx], 2)
        indx += 1
        if type_id == 0:
            sub_pkt_len = int(bits[indx:indx + 15], 2)
            indx += 15
            parse_bits = bits[indx:indx+sub_pkt_len]
            operands = []
            while(len(parse_bits) > 0):
                retval = parse_packet_header_2(parse_bits)
                operands.append(retval[0])
                parse_bits = retval[1]
            if command == 'SUM':
                inter = np.sum(operands)
            if command == 'PRD':
                inter = np.prod(operands)
            if command == 'MIN':
                inter = np.min(operands)
            if command == 'MAX':
                inter = np.max(operands)
            if command == 'GRT':
                if operands[0] > operands[1]:
                    inter = 1
                else:
                    inter = 0
            if command == 'LST':
                if operands[0] < operands[1]:
                    inter = 1
                else:
                    inter = 0
            if command == 'EQU':
                if operands[0] == operands[1]:
                    inter = 1
                else:
                    inter = 0
            return [inter, bits[indx+sub_pkt_len:]]
        else:
            sub_pkt_num = int(bits[indx:indx+11], 2)
            indx += 11
            parse_bits = bits[indx:]
            operands = []
            for i in range(sub_pkt_num):
                retval = parse_packet_header_2(parse_bits)
                operands.append(retval[0])
                parse_bits = retval[1]
            if command == 'SUM':
                inter = np.sum(operands)
            if command == 'PRD':
                inter = np.prod(operands)
            if command == 'MIN':
                inter = np.min(operands)
            if command == 'MAX':
                inter = np.max(operands)
            if command == 'GRT':
                if operands[0] > operands[1]:
                    inter = 1
                else:
                    inter = 0
            if command == 'LST':
                if operands[0] < operands[1]:
                    inter = 1
                else:
                    inter = 0
            if command == 'EQU':
                if operands[0] == operands[1]:
                    inter = 1
                else:
                    inter = 0
            return [inter, parse_bits]

with open('input.txt') as file:
    binary = ""
    for line in file:
        for char in line.strip():
            binary += format(int(char, 16), "04b")
    retval = parse_packet_header_2(binary)
    print('Part 2: ' + str(retval[0]))

