from decimal import Context, Decimal, getcontext, setcontext

one = Decimal('1')
three = Decimal('3')
original_context = getcontext()
context = Context(prec=5)
setcontext(context)
print(context)
print(one / three)
setcontext(original_context)
print(one / three)