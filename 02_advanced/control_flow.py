import random

def high_low_game():
    print("Welcome to the High-Low Game!")
    print("---------------------------------------------------------------")
    point = 0
    Round = 1
    wining_point = 5
    while True:

        if wining_point == point:
            print("Wow! You played perfectly!")
            print("You won the game!")
            break

        computer_number = random.randint(1, 100)
        user_number = random.randint(1, 100)

        print(f"Round {Round}")
        print(f"Your number is {user_number}")
        user_input = input("Do you think your number is higher or lower than the computer's?: ").lower()

        if (computer_number < user_number) & (user_input == "lower"):
            print(f"you were right! The Computer number is {computer_number}")
            point += 1
            print(f"Your point is {point}")
            Round += 1
        elif (computer_number > user_number) & (user_input == "higher"):
            print(f"you were right! The Computer number is {computer_number}")
            point += 1
            print(f"Your point is {point}")
            Round += 1
        else:
            print(f"you were wrong! The Computer number is {computer_number}")
            print(f"Your final point is {point}")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                if point < 5:
                    print(f"You lose the game for Points {wining_point - point}")
                print("\nThanks for playing")
                break
            else:
                point = 0
                Round = 1

high_low_game()

