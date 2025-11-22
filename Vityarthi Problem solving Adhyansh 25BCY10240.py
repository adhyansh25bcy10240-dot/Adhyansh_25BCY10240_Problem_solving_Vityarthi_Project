import random
passes={}
def generate_password(length_pass,alphabets,num,symbols):
    alphabets="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num="0123456789"
    symbols="!@#$%^&*"
    code=""

    first_char = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    code=code+alphabets
    
    code=code+num
    if symbols:
        code=code+symbols

    password=first_char
    for i in range(length_pass):
        password=password+random.choice(code)

    return password 

a=1
while a==1:
    length_pass=int(input("Enter length of the password required:"))

    if length_pass < 8:
        print("Password length too short! Setting it to minimum length 8.")
        length_pass = 8

    symbols=input("should password have symbols:(yes/no)").lower()=="yes"


    KeyName=input("Enter the platform name to store this password:")

    password=generate_password(length_pass,True,True,symbols)

    passes[KeyName]=password
    print("Your Password is:",password)

    print("If you want to view your passwords,enter the platform name:")
    isthere=input("Enter Platform name:")

    if isthere in passes:
        print(f"Password for the following Platform,{isthere} is:{passes[isthere]}")

    else:
        print("Password for following platform is not there")

    repeat=input("Enter (yes/no) to enter one more password:").lower()
    if repeat=="no":
         break


