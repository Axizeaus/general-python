from functools import wraps

def max_results(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print(
                    f'Result is too big {result}. '
                    f'Max result allowed is {threshold}.'
                )
            return result
        return wrapper
    return decorator

@max_results(75)
def cube(n):
    return n ** 3

print(cube(5))