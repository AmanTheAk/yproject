import string, random

opt = input("\n***What you want in your password***\n1.Small-Letters\n2.Capital_Letters\n3.Digits\n4.Punctuation-Marks\nChoose options : ")

chars = []
if "1" in opt:
    chars.append(string.ascii_lowercase)
if "2" in opt:
    chars.append(string.ascii_uppercase)
if "3" in opt:
    chars.append(string.digits)
if "4" in opt:
    chars.append(string.punctuation)
chars = ''.join(chars)

pLen = int(input("\nEnter length of password : "))
nop = int(input("\nEnter the number of password you want to generate : "))

file = open('C:/Users/amant/Desktop/pList.txt', 'w')

for pGen in range(nop):
    pGen = random.choices(chars, k = pLen)
    pGen = f"{''.join(pGen)}\n"
    file.write(pGen)





# pLen = password Length 
# opt = options 
# chars = characters
# nop = number of password 
# pGen = password generate 
