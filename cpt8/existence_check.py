from pathlib import Path

p = Path('poem.txt')
print(p)
print(p.parent)
path = p.parent.absolute()
print('*' * 10)
print(p.is_file())
print(path)
print(path.is_dir())
q = Path('/home/Axizeaus/Projects/python-intermediate/cpt8')
print(q.is_dir())
print('*' * 10)
print(q)