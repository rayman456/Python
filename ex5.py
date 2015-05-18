import time

while True:
    useless = input("press enter...")
    letter = ord("a")
    value = int(time.time() % 26)
    letter = chr(letter + value)
    print("your random letter is ", letter)
    
