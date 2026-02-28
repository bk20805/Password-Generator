import string
import secrets
import random

def generate_pass(length):
    """Generate a secure random password of given length."""
    chars = string.ascii_letters + string.digits + string.punctuation
    p_chars= [secrets.choice(string.ascii_lowercase),secrets.choice(string.ascii_uppercase), secrets.choice(string.digits), secrets.choice(string.punctuation)]
    for i in range(length-4):
        p_chars.append(secrets.choice(chars))

    random.shuffle(p_chars)

    password=""
    for i in p_chars:
        password+=i
    return password

while True:
    length_inp=input("Enter length of password(minimum length should be 8):")
    if length_inp.isdigit()==False:
              print("Please enter a valid length.")
              continue
    length=int(length_inp)
    if length<8:
        print("Password length must be at least 8.")
        continue

    print("Your randomly generated password:",generate_pass(length))
    cont = input("Do you want to continue? Y/N: ")
    while cont not in ('y','Y','n','N'):
        print("Enter a valid choice.")
        cont = input("Do you want to continue? Y/N: ")
    if cont in ('n','N'):
        print("Thank you for using this password generator!")
        break
        

    


    
