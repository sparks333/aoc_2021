

from os import sep


with open('input.txt') as file:

    valid_digits = 0

    for line in file:
      inout = line.split('|')
      input = inout[0].split()
      output = inout[1].split()
      for i in output:
          if len(i) == 2:
              valid_digits += 1
          if len(i) == 3:
              valid_digits += 1
          if len(i) == 4:
              valid_digits += 1
          if len(i) == 7:
              valid_digits += 1

    print('Part 1: ' + str(valid_digits))

with open('input.txt') as file:
    
    numbers = dict()

    digit_sum = 0

    for line in file:
      sub_digit = 0
      inout = line.split('|')
      input = inout[0].split()
      output = inout[1].split()
      for i in input:
        if len(i) == 2:
            numbers['1'] = i
        if len(i) == 3:
            numbers['7'] = i
        if len(i) == 4:
            numbers['4'] = i
        if len(i) == 7:
            numbers['8'] = i

      for i in input:

          intersect_1 = set(i).intersection(numbers['1'])
          intersect_4 = set(i).intersection(numbers['4'])
          intersect_7 = set(i).intersection(numbers['7'])

          if len(i) == 5:
              if len(intersect_7) == 3:
                numbers['3'] = i
              else:
                  if len(intersect_4) == 2:
                      numbers['2'] = i
                  else:
                      numbers['5'] = i

          if len(i) == 6:
              if len(intersect_7) == 3:
                  if len(intersect_4) == 4:
                    numbers['9'] = i
                  else:
                    numbers['0'] = i
              else:
                  numbers['6'] = i
         
                  
      for i in output:
          for val in numbers:
              if len(set(i).intersection(numbers[val])) == max(len(i), len(numbers[val])):
                sub_digit = (sub_digit * 10) + int(val)
                break

      digit_sum += sub_digit

    print('Part 2: ' + str(digit_sum))