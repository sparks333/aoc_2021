with open('input.txt') as file:

    score = 0

    for line in file:

        stack = []

        for ch in line:
            if ch == '(' or ch == '{' or ch == '[' or ch == '<':
                stack.append(ch)
            elif ch == '\n':
                continue
            else:
                open_char = stack.pop()
                if not ((open_char == '(' and ch == ')') or \
                        (open_char == '[' and ch == ']') or \
                        (open_char == '{' and ch == '}') or \
                        (open_char == '<' and ch == '>')):
                    if ch == ')':
                        score += 3
                    if ch == ']':
                        score += 57
                    if ch == '}':
                        score += 1197
                    if ch == '>':
                        score += 25137
                    break

print('Part 1: ' + str(score))

with open('input.txt') as file:

    scores = []

    for line in file:

        stack = []
        sub_score = 0

        for ch in line:
            if ch == '(' or ch == '{' or ch == '[' or ch == '<':
                stack.append(ch)
            elif ch == '\n':
                while len(stack) > 0:
                    sub_score *= 5
                    open_char = stack.pop()
                    if open_char == '(':
                        sub_score += 1
                    if open_char == '[':
                        sub_score += 2
                    if open_char == '{':
                        sub_score += 3
                    if open_char == '<':
                        sub_score += 4
            else:
                open_char = stack.pop()
                if not ((open_char == '(' and ch == ')') or \
                        (open_char == '[' and ch == ']') or \
                        (open_char == '{' and ch == '}') or \
                        (open_char == '<' and ch == '>')):
                    break
        if sub_score > 0:
            scores.append(sub_score)
scores.sort()
score = scores[int(len(scores)/2)]

print('Part 2: ' + str(score))