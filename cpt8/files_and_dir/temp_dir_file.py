from tempfile import NamedTemporaryFile, TemporaryDirectory
with TemporaryDirectory(dir='.') as td:
    print('Temp dir:' , td)
    with NamedTemporaryFile(dir=td) as t:
        name = t.name
        print(name)