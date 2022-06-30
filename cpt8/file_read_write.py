with open('poem.txt') as f:
    lines = [line.rstrip() for line in f]

with open('poem_copy.txt', 'w') as fw:
    fw.write('\n'.join(lines))