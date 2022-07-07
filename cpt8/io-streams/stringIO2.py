import io

with io.StringIO() as stream:
    stream.write('This is Python Samurai')
    print(' and this is Python Ninja',file=stream)
    content = stream.getvalue()
    print(content)