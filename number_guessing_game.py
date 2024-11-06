import random

def number_guessing_game(user_name):

    game_count = 0
    game_win = 0
    game_lose = 0

    print(f"\n{user_name}, Welcome to number guessing game.")

    def game():
        computer_choice = random.randint(1,3)
        while True:
            try:
                user_choice = int(input("\nGuess a number from 1 to 3: "))
                break
            except ValueError:
                print("\nInvalid choice. Guess a number from 1 to 3.")

        if user_choice < 1 or user_choice > 3:
            print("\nInvalid choice. Guess a number from 1 to 3.")
            return game()
        else:
            nonlocal game_count, game_win, game_lose
            game_count += 1
            print(f"\nComputer Choice = {computer_choice}")
            print(f"User Choice = {user_choice}\n")
            if computer_choice == user_choice:
                game_win += 1
                print("Win🎉")
            else:
                game_lose += 1
                print("Lose😔")

            flag = True
            while flag:
                rematch = input("\nDo you want to play again?\n\tEnter 'Y' to continue and 'N' to quit: ")
                if rematch in ['Y', 'y']:
                    print("\n**********************************")
                    return game()
                elif rematch in ['N', 'n']:
                    print("\n********** Game Result **********")
                    print(f"\nGame Count: {game_count}")
                    print(f"Wins: {game_win}")
                    print(f"Loses: {game_lose}\n")
                    flag = False
                else:
                    print(f"\nInvalid choice.")


    return game

name = input("Enter your name: ")
player = number_guessing_game(name)
player()