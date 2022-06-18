values = (10, "yes")
try: 
    q, r = divmod(*values)
except (ZeroDivisionError, TypeError) as e:
    print(type(e), e)
    
    
values = (10, 0)
try:
    q, r = divmod(*values)
except ZeroDivisionError as e:
    print(type(e), e)
except TypeError as te:
    print(type(te), te)
finally:
    print("Finally...")