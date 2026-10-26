# Maximum number from the list

user_list = input("Enter numbers with spaces: ")
user_list_split = user_list.split()
#print(user_list_split)

count = 0
for number in user_list_split:
    count += 1
#print(count)

for i in range(count):
    user_list_split[i] = int(user_list_split[i])
print(user_list_split)

max_number = user_list_split[0]

for num in user_list_split:
    if num > max_number:
        max_number = num
print(f"Maximum number is : {max_number}")