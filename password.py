import random as rand

def genPassword(length):
    characters = ["qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!~`@#$%^&*();"]

    output = []
    

    for i in range(length):
        output += rand.choice(characters)

    print("Your password is:", output)

rand.seed()

print("Enter an integer length for the password: ")
input = input()
num = int(input)
genPassword(num)