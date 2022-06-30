from collections import Counter
from string import ascii_letters

chars = ascii_letters + ' '

print(chars)


def sanitize(s, chars):
    return ''.join(c for c in s if c in chars )

def reverse(s):
    return s[::-1]

with open('poem.txt') as fh:
    lines = [line.rstrip() for line in fh]
    
with open('meop.txt', 'w') as fh:
    fh.write('\n'.join(reverse(line) for line in lines))
    
lines = [sanitize(line, chars) for line in lines]
whole = ''.join(lines)

cnt = Counter(whole.lower().split())
print(cnt.most_common(3))