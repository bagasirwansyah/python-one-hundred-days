""" Project of Day 5: PyPassword Generator """

import random

print("Welcome to the PyPassword Generator!")
letter = int(input("How many letters would you like in your password?\n"))
symbol = int(input("How many symbols would you like?\n"))
number = int(input("How many numbers would you like?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

final_pass = ''
eligible = [1,2,3]

if letter == 0:
    eligible.remove(1)
if number == 0:
    eligible.remove(2)
if symbol == 0:
    eligible.remove(3)

for i in range(letter + symbol + number):
    chr = random.choice(eligible)
    if chr == 1:
        final_pass += random.choice(letters)
        letter -= 1
        if letter == 0:
            eligible.remove(1)
    elif chr == 2:
        final_pass += random.choice(numbers)
        number -= 1
        if number == 0:
            eligible.remove(2)
    else:
        final_pass += random.choice(symbols)
        symbol -= 1
        if symbol == 0:
            eligible.remove(3)


print(f"Here is your password: {final_pass}")
