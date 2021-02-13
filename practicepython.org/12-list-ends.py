"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
"""

def new_list(lst):
  new_list = []
  new_list.append(lst[0])
  new_list.append(lst[-1])
  return new_list


a = [5, 10, 15, 20, 25]
print(new_list(a))