def palindrom(word_to_checkt):
    """
       Checking is argument is palindrome:
       arguments:
       word_to_checkt
    """
    if list(word_to_checkt) == list(word_to_checkt[::-1]):
        return True
    else:
        return False


print("Program sprawdza czy podane słowo jest palindromem tj. czy brzmi ono tak samo pisane od lewej do prawej jak rowniez od prawej do lewej")
text = str(input("Proszę podać słowo do sprawdzenia:\n").lower())
word = palindrom(text)

if word == True:
    print(f"Słowo {text} jest pailindromem")
else:
    print(f"Słowo {text} nie jest palindromem")
