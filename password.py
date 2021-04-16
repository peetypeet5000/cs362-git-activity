import random as rand

def genPassword(length):
    characters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!~`@#$%^&*();/.,}[{]"
    
    print("Your password is: ")
    print("".join(rand.choices(characters, k =length)))

rand.seed()

print("Enter an integer length for the password: ")
input = input()
num = int(input)
genPassword(num)