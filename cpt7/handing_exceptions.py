def try_syntex(numerator, denominator):
    try:
        print(f"in the try block: {numerator}/{denominator}")
        result = numerator / denominator
    except ZeroDivisionError as zde:
        print(zde)
    else:
        print("The result is:", result)
        return result
    finally:
        print('Exiting')
        
print(try_syntex(14, 2))
print(try_syntex(10, 0))