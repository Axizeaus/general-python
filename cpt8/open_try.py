try:
    file_handle = open('poem.txt', 'r')
except FileNotFoundError as e:
    print(e)
    
try:
    for line in file_handle.readlines():
        print(line.strip())

finally:
    file_handle.close()