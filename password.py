import random

def genPassword(len):
    characters = ["qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!~`@#$%^&*();"]

    output = []

    for i in range(len):
        output += characters[random.choice(characters)]
    pass

random.seed()

print("Enter an integer length for the password: ")
input = input()
num = int(input)
genPassword(num)