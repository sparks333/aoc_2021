import ast
import math
import re

def isNum(st):
    return st != '[' and st != ']'

def calcMag(res):
    while len(res) > 1:
        index = 0
        while index < len(res)-1:
            if isNum(res[index]) and isNum(res[index+1]):
                left = float(int(res[index]))
                right = float(int(res[index+1]))
                del res[index:index+3]
                res[index-1] = str(int(3*left + 2*right))
                break
            index += 1




def pretty_print(res):
    for i in range(len(res)):
        if i == 0:
            print(res[i], end='')
        elif res[i-1] == '[' and res[i] == '[':
            print(res[i], end='')
        elif res[i-1] == '[' and isNum(res[i]):
            print(res[i], end='')
        elif res[i-1] == ']' and res[i] == '[':
            print(',' + res[i], end='')
        elif res[i-1] == ']' and isNum(res[i]):
            print(',' + res[i], end='')
        elif res[i-1] == ']' and res[i] == ']':
            print(res[i], end='')
        elif isNum(res[i-1]) and res[i] == '[':
            print(',' + res[i], end='')
        elif isNum(res[i-1]) and isNum(res[i]):
            print(',' + res[i], end='')
        elif isNum(res[i-1]) and res[i] == ']':
            print(res[i], end='')
        else:
            print('SOMETHING BAD HAS HAPPENED HERE')
    print()



def reduce(res):
    while True:
        level = 0
        index = 0
        changed = False
        while index < len(res) and changed == False:
            if res[index] == '[':
                level += 1
                index += 1
            elif isNum(res[index]) and isNum(res[index+1]):
                if level >= 5:
                    add_left = int(res[index])
                    add_right = int(res[index+1])
                    del res[index:index+3]
                    index -= 1
                    res[index] = '0'
                    sub_index_left = index-1
                    sub_index_right = index + 1
                    changed = True
                    while sub_index_left >= 0:
                        if isNum(res[sub_index_left]):
                            res[sub_index_left] = str(int(res[sub_index_left]) + add_left)
                            break
                        sub_index_left -= 1
                    while sub_index_right < len(res):
                        if isNum(res[sub_index_right]):
                            res[sub_index_right] = str(int(res[sub_index_right]) + add_right)
                            break
                        sub_index_right += 1
                    break
                index += 1
            elif res[index] == ']':
                level -= 1
                index += 1
            else:
                index += 1

        index = 0
        while index < len(res) and changed == False:
            if isNum(res[index]):
                digit = float(int(res[index]))
                if int(res[index]) > 9:
                    left = str(int(math.floor(digit/2)))
                    right = str(int(math.ceil(digit/2)))
                    res[index] = '['
                    res.insert(index+1, left)
                    res.insert(index+2, right)
                    res.insert(index+3, ']')
                    changed = True
                    break
                index += 1
            else:
                index += 1

        if changed == False:
            break

    return res

with open('input.txt') as file:

    first = True
    total = ''

    for line in file:
        num = re.findall('\[|\]|[0-9]+', line.strip())
        if first:
            total = reduce(num)
            first = False
        else:
            in_line = ['[']
            in_line.extend(total)
            in_line.extend(num)
            in_line.extend(']')

            total = reduce(in_line)
    calcMag(total)
    print('Part 1: ' + str(total[0]))

with open('input.txt') as file1:

    first = True
    total = ''
    max_mag = 0
    for line1 in file1:
        with open('input.txt') as file2:
            for line2 in file2:
                if line1 == line2:
                    continue
                num1 = re.findall('\[|\]|[0-9]+', line1.strip())
                num2 = re.findall('\[|\]|[0-9]+', line2.strip())

                in_line = ['[']
                in_line.extend(num1)
                in_line.extend(num2)
                in_line.extend(']')

                total = reduce(in_line)
                calcMag(total)
                if int(total[0]) > max_mag:
                    max_mag = int(total[0])

    print('Part 2: ' + str(max_mag))