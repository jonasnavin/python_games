import random
from enum import Enum

def rock_paper_scissors_game(user_name):

    game_count = 0
    game_win = 0
    game_lose = 0
    game_tie = 0

    print(f"\n{user_name}, Welcome to rock, paper and scissors game.")

    def game():

        computer_choice = random.choice(['ROCK', 'PAPER', 'SCISSORS'])

        while True:
            try:
                user_int = int(input("\nSelect a value from the options below.\n\t1 - ROCK\n\t2 - PAPER\n\t3 - Scissors\n"))
                break
            except ValueError:
                print("\nInvalid Choice. Choose the options from 1 to 3.")

        if user_int < 1 or user_int > 3:
            print("\nInvalid Choice. Choose the options from 1 to 3.")
            return game()
        else:
            class RPS(Enum):
                ROCK = 1
                PAPER = 2
                SCISSORS = 3

            user_choice = RPS(user_int).name

            print(f"\nUser Choice: {user_choice}")
            print(f"Computer Choice: {computer_choice}\n")

            nonlocal game_count, game_win, game_lose, game_tie

            game_count += 1

            if user_choice == computer_choice:
                game_tie += 1
                print("Tie Game 🤝")
            elif user_choice == 1 and computer_choice == 3:
                game_win += 1
                print("You Win 🎉")
            elif user_choice == 2 and computer_choice == 1:
                game_win += 1
                print("You Win 🎉")
            elif user_choice == 3 and computer_choice == 2:
                game_win += 1
                print("You win 🎉")
            else:
                game_lose += 1
                print("Computer Win 😔")

        flag = True
        while flag:
            try:
                rematch_int = int(input("Do you want to play again?\n\t1 - YES\n\t2 - NO\n"))
            except ValueError:
                print("\nInvalid choice. Choose options either 1 or 2.")
            if rematch_int == 1 or rematch_int == 2:
                class Rematch(Enum):
                    YES = 1
                    NO = 2
                rematch_choice = Rematch(rematch_int).name
                if rematch_choice == "YES":
                    print("\n*******************************")
                    return game()
                elif rematch_choice == "NO":
                    print("\n********** Game Result **********")
                    print(f"\nGame Count: {game_count}")
                    print(f"Wins: {game_win}")
                    print(f"Loses: {game_lose}")
                    print(f"Tie Game: {game_tie}")
                    flag = False
            else:
                print("\nInvalid choice. Choose options either 1 or 2.")


    return game

name = input("Enter your name: ")
player = rock_paper_scissors_game(name)
player()