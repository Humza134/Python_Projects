import random

# def main():
#     # Generate the secret number randomly between 1 and 100
#     secret_number:int = random.randint(1, 99)

#     print("I am thinking of a number between 1 and 99.")

#     guess = int(input("Enter your guess between 1 to 99: "))

#     while guess != secret_number:
#         if guess < secret_number:
#             print(guess, "Your guess is too low.")
#         else:
#             print(guess, "Your guess is too high.")
#         print("Try again.")

#         guess = int(input("Enter your new guess: "))

#     print("Congratulations! The number was: " + str(secret_number) )

# main()

allowed_attempt = 5


def main():
    user_attempt = 0
    # Generate the secret number randomly between 1 and 100
    secret_number = random.randint(1, 99)

    print("I am thinking of a number between 1 and 99.")
    
    while True:
        print(f"Attempts left: {allowed_attempt - user_attempt}")

        if (user_attempt == allowed_attempt):
            print("Game over")
            break

        guess_input = input("Enter your guess between 1 to 99 (or type 'quit' or 'q' to exit): ")
        user_attempt +=1
        # Check if the user wants to quit
        if guess_input.lower() in ['quit', 'q']:
            print("Game exited. Thanks for playing!")
            break
        
        # Convert the guess to an integer and handle non-integer inputs
        try:
            guess = int(guess_input)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 99 or 'quit' to exit.")
            continue

        # Check the guess against the secret number
        if guess == secret_number:
            print("Congratulations! The number was:", secret_number)
            break
        elif guess < secret_number:
            print(guess, "is too low.")
        else:
            print(guess, "is too high.")

        print("Try again.")

main()

