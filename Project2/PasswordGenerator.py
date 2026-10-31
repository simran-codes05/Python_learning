#Password Generator
import random

letter_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
               ,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

number_list = [1,2,3,4,5,6,7,8,9]

symbol_list = ['!','#','$','%','&','*','(',')','+']
print("welcome to the Password Generator!")

letters = input("How many letters you want in your password? ")

numbers = input("How many numbers you want in your password? ")

symbols = input("How many symbols you want in your password? ")

password_list = []

for i in range(1,int(letters) + 1):
    letter_str = random.choice(letter_list)
    password_list += letter_str
#print(password_list)

for i in range(1,int(numbers) + 1):
    num_str = random.choice(number_list)
    password_list += str(num_str)
#print(password_list)

for i in range(1,int(symbols) + 1):
    symbol_str = random.choice(symbol_list)
    password_list += symbol_str
#print(password_list)

random.shuffle(password_list)
#print(password_list)

password = ""

for i in password_list:
    password += i
print(password)

