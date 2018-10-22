#!/user/bin/env python

# author: Mailen Bilsky
# date: 22/10/2018

# title: Guessing Game One
# url: https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random


def guess():
  """
  :return: Return a string with messege saying if the user guessed the correct
  number, and how many time it took them to guess correctly.
  :rtype: string
  """
  
  print("You can exit any time by typing 'exit'")
  print()
  random_number = random.randint(1,9)
  
  count = 0
  user_guess = 0
    
  while True:
    user_guess = (input("Guess a number from 1 to 9: "))

    if user_guess.lower() in ("exit", "e"):
      break

    if user_guess.isdigit():
        count += 1
        user_guess = int(user_guess)
        if user_guess > random_number:
          print ("You guessed too high\n")
        elif user_guess < random_number:
          print("You guessed too low\n")
        else:
          print("\nYou guessed exactly right!")
          print("\nAnd you only guessed %s times" % count)
          break
    else:
        print("Your input was invalid. Please try again.\n")


guess()