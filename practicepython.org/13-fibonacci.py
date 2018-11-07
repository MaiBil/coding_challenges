"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""


def fibonacci():
  num = int(input("How many Fibonacci numbers would you like?: "))
  i = 0
  fibonacci_sequence = []
  while i <= num:
    if i == 0 or i == 1:
      fibonacci_sequence.append(1)
    else:
      fibonacci_sequence.append(fibonacci_sequence[i-2]+fibonacci_sequence[i-1])
    i += 1
  return fibonacci_sequence[0:(len(fibonacci_sequence))-1]


if __name__ == "__main__":
  print(fibonacci())