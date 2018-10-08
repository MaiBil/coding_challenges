#!/user/bin/env python

# author: Mailen Bilsky
# date: 08/10/2018

# title: Rock Paper Scissors
# url: https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays
(using input), compare them, print out a message of congratulations to
the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

import random


def rock_paper_scissors():
    """
    :param nmultiply: None
    :type multiply: None
    :return: Return a message saying if the user won or not, and ask if
    they want to play again
    :rtype: string
    """

    play_again = "Y"
    while play_again != "n":
        user_choice = (input("Choose rock, paper or scissors: ")).lower()
        computer = random.choice(["rock", "paper", "scissors"])
        print("Computer chose %s" % computer)
        if user_choice == computer:
            print("It's a tie!")
        elif (user_choice == "rock" and computer == "scissors"):
            print("You win!")
        elif (user_choice == "scissors" and computer == "paper"):
            print("You win!")
        elif (user_choice == "paper" and computer == "rock"):
            print("You win!")
        else:
            print("You lose")
        print()
        play_again = (input("Do you want to play again? (Y/N): ")).lower()


if __name__ == '__main__':
    rock_paper_scissors()
