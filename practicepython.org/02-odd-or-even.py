#!/user/bin/env python

# author: Mailen Bilsky
# date: 03/10/2018

# title: Odd or Even
# url: https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
# time complexity: O(n), with n being the amount of numbers in the input string

def parity(num):
  """
  Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

  Extras:

  1. If the number is a multiple of 4, print out a different message.
  """

  if int(numb) % 4 == 0:
    print ("Your number is a multiple of 4.")
  elif int(numb) % 2 == 0:
    print ("The number you chose is even.")
  else:
    print ("The number you chose is odd.")

numb = input("Choose a number: ")
parity(numb)

print ()
def checking(num,check):
  """
  Extras:

  2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
  """
  
  if int(check) % int(num) == 0:
    print("Check divides evenly into num.")
  else:
    print("Check does not divide evenly into num.")

num = input("Now choose a number, we'll call it 'num': ")
check = input("Choose another number, we'll call it 'check': ")
checking(num,check)