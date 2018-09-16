#!/user/bin/env python

# author: Mailen Bilsky
# date: 11/09/2018

# title: Replace With Alphabet Position
# url: https://www.codewars.com/kata/546f922b54af40e1e90001da
# difficulty: 6 kyu
# time complexity: O(n), with n being the amount of numbers in the input string

def alphabet_position(text):
    """
    In this kata you are required to, given a string, replace every letter with its position in the alphabet.

    If anything in the text isn't a letter, ignore it and don't return it.

    a being 1, b being 2, etc.

    :param nmultiply: String with text
    :type multiply: string
    :return: String replacing every letter with its position in the alphabet.
    :rtype: string
    """

  num = ""
  for a in text:
    if a in "abcdefghijklmnopqrstuvwxyz":
      if a == "a":
        num = num + "1 "
      elif a == "b":
        num = num + "2 "
      elif a == "c":
        num = num + "3 "
      elif a == "d":
        num = num + "4 "
      elif a == "e":
        num = num + "5 "
      elif a == "f":
        num = num + "6 "
      elif a == "g":
        num = num + "7 "
      elif a == "h":
        num = num + "8 "
      elif a == "i":
        num = num + "9 "
      elif a == "j":
        num = num + "10 "
      elif a == "k":
        num = num + "11 "
      elif a == "l":
        num = num + "12 "
      elif a == "m":
        num = num + "13 "
      elif a == "n":
        num = num + "14 "
      elif a == "o":
        num = num + "15 "
      elif a == "p":
        num = num + "16 "
      elif a == "q":
        num = num + "17 "
      elif a == "r":
        num = num + "18 "
      elif a == "s":
        num = num + "19 "
      elif a == "t":
        num = num + "20 "
      elif a == "u":
        num = num + "21 "
      elif a == "v":
        num = num + "22 "
      elif a == "w":
        num = num + "23 "
      elif a == "x":
        num = num + "24 "
      elif a == "y":
        num = num + "25 "
      elif a == "z":
        num = num + "26 "
  return num[:-1]