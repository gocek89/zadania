def palindrom(word):
    if list(word) == list(word[::-1]):
        return True
    else:
        return False
