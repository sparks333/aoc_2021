with open('input.txt') as file:
    state = 0    
    rules = {}
    for line in file:
        if line == '\n':
            state = 1;
            continue
        if state == 0:
            formula = line.strip()
        else:
            rule = line.strip().split(' -> ')
            rules[rule[0]] = rule[1]

for steps in range(10):
    output = formula[0]
    for i in range(len(formula) - 1):
        if formula[i:i+2] in rules:
            output += rules[formula[i:i+2]]
        output += formula[i+1]
    formula = output

char_freq = {}
for i in formula:
    if i in char_freq:
        char_freq[i] += 1
    else:
        char_freq[i] = 1

sorted_chars = sorted(char_freq.items(), key=lambda kv:(kv[1], kv[0]))

print('Part 1: ' + str(sorted_chars[-1][1] - sorted_chars[0][1]))

with open('input.txt') as file:
    state = 0    
    rules = {}
    for line in file:
        if line == '\n':
            state = 1;
            continue
        if state == 0:
            formula = line.strip()
        else:
            rule = line.strip().split(' -> ')
            rules[rule[0]] = rule[1]

strmap = {}
for i in range(len(formula)-1):
    if formula[i:i+2] in strmap:
        strmap[formula[i:i+2]] += 1
    else:
        strmap[formula[i:i+2]] = 1

for steps in range(40):
    new_strmap = {}
    for string in strmap:
        new_char = rules[string]
        new_string_1 = string[0] + new_char
        new_string_2 = new_char + string[1]
        if new_string_1 in new_strmap:
            new_strmap[new_string_1] += strmap[string]
        else:
            new_strmap[new_string_1] = strmap[string]
        if new_string_2 in new_strmap:
            new_strmap[new_string_2] += strmap[string]
        else:
            new_strmap[new_string_2] = strmap[string]
    strmap = new_strmap

char_total = {}
for i in strmap:
    if i[0] in char_total:
        char_total[i[0]] += strmap[i]
    else:
        char_total[i[0]] = strmap[i]
    if i[1] in char_total:
        char_total[i[1]] += strmap[i]
    else:
        char_total[i[1]] = strmap[i]
char_total[formula[-1]] += 1
sorted_chars = sorted(char_total.items(), key=lambda kv:(kv[1], kv[0]))

print('Part 2: ' + str(int((sorted_chars[-1][1] - sorted_chars[0][1])/2)))
