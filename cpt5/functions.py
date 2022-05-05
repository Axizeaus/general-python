def gcd(a, b):
    """Calculate the greatest common divisor"""
    while b != 0:
        a, b = b , a % b
    return a

N = 50 
triples = sorted(
    ((a,b,c) for a, b, c in (
        ((m**2 - n**2), (2 * m * n), (m ** 2 + n ** 2))
        for m in range(1, int(N**5) + 1) 
        for n in range(1, m)
        if (m - n) % 2 and gcd(m, n) == 1
    ) if c <= N), key=sum
)

print(triples)

# the above code is quite a pain

# def gen_triples(N):
#     for m in range(1, int(N**.5) + 1):                  
#         for n in range(1, m):                           
#             if (m - n) % 2 and gcd(m, n) == 1:          
#                 c = m**2 + n**2                         
#                 if c <= N:                              
#                     a = m**2 - n**2                     
#                     b = 2 * m * n                       
#                     yield (a, b, c)                    
# print(sorted(gen_triples(50), key=sum))                 