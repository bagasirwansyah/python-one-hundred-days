""" Project of Day 4: Rock Paper Scissor """

import random

# I got the graphics from https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe
# This graphics is not mine and all rights belong to the owner

rock = """
       _______
------'   ____)
         (_____)
         (_____)
         (____)
------.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissor]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))
print(choices[user])

computer = random.randint(0,2)
print("Computer chose:")
print(choices[computer])

user_rock = ["Draw", "Lose", "Win"]
user_paper = ["Win", "Draw", "Lose"]
user_scissor = ["Lose", "Win", "Draw"]
the_result = [user_rock, user_paper, user_scissor]

print("You {}".format(the_result[user][computer]))
