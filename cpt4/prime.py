from math import sqrt, ceil

def get_prime(n):
    """Calculate a list of primes up to n (included). """
    prime_list = list()
    for num in range(2, n+1):
        is_prime = True
        root = ceil(sqrt(num))
        for prime in prime_list:
            if prime > root:
                break
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)
    return prime_list

print(get_prime(50))