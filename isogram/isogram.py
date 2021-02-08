def is_isogram(string):

    string_letters = [i.lower() for i in string if i.isalpha()]

    a = ''.join(string_letters)
    b = set(''.join(string_letters))
    return sorted(a) == sorted(b)