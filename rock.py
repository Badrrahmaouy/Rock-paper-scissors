#!/usr/bin/env python3
import random
from colorama import Fore, Style

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']
"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, heir_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        choice = input("Rock, paper, scissors? > ").lower()
        while choice not in moves:
            print("Choice not valid")
            choice = input("Rock, paper, scissors? > ").lower()
        return choice


class ReflectPlayer(Player):
    def __init__(self):
        self.my_move = "None"

    def learn(self, my_move, their_move):
        self.my_move = my_move

    def move(self):
        if self.my_move == "None":
            return random.choice(moves)
        else:
            return self.my_move


class CyclePlayer(Player):
    def __init__(self):
        self.their_move = "None"

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move == "rock":
            return "scissors"
        elif self.their_move == "scissors":
            return "paper"
        elif self.their_move == "paper":
            return "rock"
        else:
            return random.choice(moves)


def choosePlayer():
    players = {
        "1": Player(),
        "2": RandomPlayer(),
        "3": CyclePlayer(),
        "4": ReflectPlayer()
    }
    choices = ["1", "2", "3", "4"]
    user_choice = input("Select who you want to play against:\n"
                        "1- Rock Player\n"
                        "2- Random Player\n"
                        "3- Cycle Player\n"
                        "4- Reflect Player\n")
    while user_choice not in choices:
        print("Choice not valid!")
        user_choice = input("Select who you want to play against:\n"
                            "1- Rock Player\n"
                            "2- Random Player\n"
                            "3- Cycle Player\n"
                            "4- Reflect Player\n")
    return players[user_choice]


def beats(one, two):
    if one == 'rock' and two == 'scissors':
        print("** " + Fore.BLUE + "PLAYER 1 " + Style.RESET_ALL + "WINS **")
        return 1
    elif one == 'scissors' and two == 'paper':
        print("** " + Fore.BLUE + "PLAYER 1 " + Style.RESET_ALL + "WINS **")
        return 1
    elif one == 'paper' and two == 'rock':
        print("** " + Fore.BLUE + "PLAYER 1 " + Style.RESET_ALL + "WINS **")
        return 1
    elif one == two:
        print("** TIE! **")
        return 0
    else:
        print("** " + Fore.RED + "PLAYER 2 " + Style.RESET_ALL + "WINS **")
        return 2
    # return ((one == 'rock' and two == 'scissors') or
    #         (one == 'scissors' and two == 'paper') or
    #         (one == 'paper' and two == 'rock'))


def Howmany():
    gameTime = input("How many times would you like to play?\n")
    while True:
        try:
            gameTime = int(gameTime)
            break
        except ValueError:
            print("Choice not valid!")
            gameTime = input("How many times would you like to play?\n")
    return gameTime


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print("Player 1: " + Fore.BLUE + f"{move1} " + Style.RESET_ALL +
              "Player 2: " + Fore.RED + f"{move2}" + Style.RESET_ALL)
        print(f"You played {move1}.")
        print(f"Opponent played {move2}.")
        self.p2.learn(move1, move2)    # learn move for CyclePlayer
        result = beats(move1, move2)
        if result == 1:
            return 1
        elif result == 2:
            return 2

    def Winner(self, score1, score2):
        if score1 > score2:
            print("The winner is: " + Fore.BLUE + "PLAYER 1" +
                  Style.RESET_ALL + "!!")
        elif score1 == score2:
            print("Nobody wins!")
        else:
            print("The winner is: " + Fore.RED + "PLAYER 2" +
                  Style.RESET_ALL + "!!")
        print("The final score is: " + Fore.BLUE + f"player 1 ({score1})\t "
              + Fore.RED + f"player 2 ({score2})" + Style.RESET_ALL)

    def play_game(self):
        score1 = 0
        score2 = 0
        print("Game start!")
        gameTime = Howmany()
        for round in range(gameTime):
            print(f"Round {round + 1} -- ")
            round = self.play_round()
            if round == 1:
                score1 += 1
            elif round == 2:
                score2 += 1
            print("Score: " + Fore.BLUE + f"player 1 |{score1}|" +
                  Style.RESET_ALL + ", " + Fore.RED + f"player 2 |{score2}|" +
                  Style.RESET_ALL)
            print()
        print("Game over!")
        self.Winner(score1, score2)


if __name__ == '__main__':
    player_choosed = choosePlayer()
    game = Game(HumanPlayer(), player_choosed)
    game.play_game()
