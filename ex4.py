import random

while True:
    useless = input("PRESS ENTER...")
    letterOrd = random.randint(ord("A"), ord("Z"))
    letter = chr(letterOrd)
    print("YOUR RANDOM LETTER IS", letter)
