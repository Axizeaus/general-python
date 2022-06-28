class StringUtil:
    @staticmethod
    def is_palindrome(s, case_sensitive = True):
        # only numbers and letters are allowed 
        s = ''.join(c for c in s if c.isalnum())
        # for case insensitive comparison, we lower-case s
        if case_sensitive:
            s = s.lower()
        for c in range(len(s) // 2):
            if s[c] != s[-c -1]:
                return False
        return True
    
    @staticmethod
    def get_unique_words(sentence):
        return set(sentence.split())
    
print(StringUtil.is_palindrome('Reder',case_sensitive=False))
print(StringUtil.is_palindrome('A nut for a jar of tuna'))  # True
print(StringUtil.is_palindrome('Never Odd, Or Even!'))  # True
print(StringUtil.is_palindrome(
    'In Girum Imus Nocte Et Consumimur Igni')  # Latin! Show-off!
) 
print(StringUtil.get_unique_words(
    'I love palindromes. I really really love them!'))

# something_interesting = 
