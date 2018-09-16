#!/user/bin/env python

# author: Mailen Bilsky
# date: 11/09/2018

# title: Complementary DNA
# url: https://www.codewars.com/kata/554e4a2f232cdd87d9000038
# difficulty: 7 kyu
# time complexity: O(n), with n being the amount of numbers in the input string

def DNA_strand(dna):
  """
  In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with 
  one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand 
  is never empty or there is no DNA at all (again, except for Haskell).

  :param nmultiply: String with "A" "T" "C" "G"
  :type multiply: string
  :return: complementary string of input
  :rtype: string
  """

  comp = ""
  for i in dna:
    if i == "A":
      comp = comp + "T"
    elif i == "T":
      comp = comp + "A"
    elif i == "C":
      comp = comp + "G"
    elif i == "G":
      comp = comp + "C"
  return comp