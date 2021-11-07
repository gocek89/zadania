def palindrom(word):
    """
       Checking is argument is palindrome:
       arguments:
       word 
    """
    if list(word) == list(word[::-1]):
        return True
    else:
        return False
