"""
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
"""


def divisors(hi):
    return [x for x in range(1, hi+1) if hi % x == 0]


def prime(num):
  divisors_list = [x for x in range(1, num+1) if num % x == 0]
  if len(divisors_list) <= 2:
    print("Your number is prime")
  else:
    print("Your number isn't prime")


num = int(input("Choose a number: "))

if __name__ == "__main__":
  prime(num)