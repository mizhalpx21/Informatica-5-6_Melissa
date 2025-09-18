# i = input 
# o = output
# names = []

# for i in range(3):  #i = position of the list
#     #name = input("Write your name: ")
#     # print(f"{i}.Hello {name}")
#     #names.append(name)
#     names.append(input("Write your name: "))

# for name in sorted(names):
#     print(f"Hello {name}")

# name = input("Write your name: ")
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# with open("names.txt", "a") as file:
#     file.write(f"{input("What is your name?")}")

with open("names.txt", "r") as file:
    lines = file.readlines()         #read each line to make a list

for line in lines: 
    print(f"Hello{line.rstrip()}")   #adds a hello in each line