import io

stream = io.StringIO()
stream.write('Learn Python Programming\n')
print('Become a Python Ninja', file=stream)
contents = stream.getvalue()
print('*' * 4)
print(contents)
stream.close()