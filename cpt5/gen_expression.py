cubes = [k**3 for k in range(5)]
print(cubes)
print(type(cubes))

cubes_gen = (k ** 3 for k in range(5))
print(cubes_gen)
print(type(cubes_gen))
print(list(cubes_gen))
print(list(cubes_gen)) # exhausted gen thus empty