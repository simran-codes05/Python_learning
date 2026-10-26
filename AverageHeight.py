user_height = input("enter your height with sapce: ")
user_height_list = user_height.split()

count = 0

for heights in user_height_list:
    count = count + 1
print(count)

for i in range(count):
    user_height_list[i] = int(user_height_list[i])
    
total = 0
for height in user_height_list :
    total += height

avg = total / count
print(round(avg))

    
