with open('poem.txt') as fh:
    print(fh)
    for line in fh:
        print(line.strip())