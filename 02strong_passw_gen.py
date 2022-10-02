import string, random

p_len = int(input("Enter password length : "))
ch = string.printable

pas = random.choices(ch, k=p_len)
print(f"Your strong password is : {''.join(pas)}")
