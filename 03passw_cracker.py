import string, random

pasw = input("Enter your password : ")
ch = string.printable

while True:
    pGuess = random.choices(ch, k=len(pasw))
    pGuess = ''.join(pGuess)
    print(pGuess)

    if pasw == pGuess:
        print(f"\nMatched password is : {pGuess}")
        break
