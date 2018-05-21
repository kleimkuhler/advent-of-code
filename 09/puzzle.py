import re

def score(stream):
    score = 0
    stack = 0
    for char in stream:
        if char == '{':
            stack += 1
        else:
            score += stack
            stack -= 1
    return score

input = open('./input.txt')
original = input.read()
canceled = re.sub(r'!.', '', original)
cleaned = re.sub(r'<.*?>', '', canceled)
final = re.sub(r',', '', cleaned)

print('a: {}'.format(score(final)))

partial_cleaned = re.sub(r'<.*?>', '<>', canceled)
print('b: {}'.format(len(canceled) - len(partial_cleaned)))
