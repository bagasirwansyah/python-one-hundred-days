""" This file is functioning as scrap paper """

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        print("Child ticket are $5.")
        price = 5
    elif age <=18:
        print("Youth ticket are $7.")
        price = 7
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
        price = 0
    else:
        print("Adult ticket are $12.")
        price = 12

    wants_photo = input("Do you want to a photo taken? Y or N. ")
    if wants_photo == 'Y':
        price += 3
    print(f"Your final bill is {price}")

else:
    print("Sorry, you have to grow taller before you can ride.")
