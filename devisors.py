def findDevisors(num):
    for i in range(1, num + 1):
        if(num % i == 0):
            print(i, "is a devisor")


print("enter a number: ")
input = input()
num = int(input)
findDevisors(num)
    