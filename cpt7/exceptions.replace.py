class NotFoundError(Exception):
    pass

vowels = {'a' : 11, 'e' : 12, 'i' : 13, 'o' : 14, 'u' : 15}

try :
    pos = vowels['y']
except NotFoundError:
    raise NotFoundError(*NotFoundError.args)

