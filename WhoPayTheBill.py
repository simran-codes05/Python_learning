import random

name = input("Enter your names with comma : ")
name_list = name.split(",")
print(name_list)

choice = random.choice(name_list)
print(f"\n{choice} will pay the bill.\n")

#without choice function
length = len(name_list)
name_choice = random.randint(0, length - 1)
print(f"{name_list[name_choice]} will pay the bill.")