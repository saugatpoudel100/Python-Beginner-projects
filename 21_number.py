import sys

# Function to end the game when the player loses
def lose_game():
    print("\nYOU LOSE!")
    print("Better luck next time!")
    sys.exit(0)

# Function to check if a list of numbers are consecutive
def is_consecutive(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i - 1] != 1:
            return False
    return True

# Function to find the nearest multiple of 4 greater than or equal to the given number
def nearest_multiple_of_4(num):
    if num >= 4:
        return num + (4 - (num % 4))
    else:
        return 4

# Main game logic
def play_game():
    sequence = []  # Stores the ongoing number sequence
    last_number = 0

    print("Enter 'F' to go First, or 'S' to go Second:")
    choice = input("> ").upper()

    if choice == "F":
        # Player goes first
        while True:
            if last_number == 20:
                lose_game()

            print("\nYour Turn.")
            print("How many numbers do you want to say? (1-3)")
            user_count = int(input("> "))

            if user_count < 1 or user_count > 3:
                print("Invalid input! You must choose 1 to 3 numbers.")
                lose_game()

            # User enters the numbers
            print("Enter your numbers:")
            for _ in range(user_count):
                num = int(input("> "))
                sequence.append(num)

            if not is_consecutive(sequence):
                print("Numbers are not consecutive!")
                lose_game()

            last_number = sequence[-1]

            if last_number == 21:
                lose_game()

            # Computer's turn: it says (4 - user's count) numbers
            comp_count = 4 - user_count
            print("\nComputer's Turn:")
            for i in range(1, comp_count + 1):
                sequence.append(last_number + i)

            print("Sequence after computer's turn:", sequence)
            last_number = sequence[-1]

    elif choice == "S":
        # Computer goes first
        comp_count = 1
        last_number = 0

        while last_number < 20:
            # Computer's turn
            print("\nComputer's Turn:")
            for i in range(1, comp_count + 1):
                sequence.append(last_number + i)
            print("Sequence after computer's turn:", sequence)

            if sequence[-1] == 20:
                lose_game()

            # Player's turn
            print("\nYour Turn.")
            print("How many numbers do you want to say? (1-3)")
            user_count = int(input("> "))

            print("Enter your numbers:")
            for _ in range(user_count):
                num = int(input("> "))
                sequence.append(num)

            if not is_consecutive(sequence):
                print("Numbers are not consecutive!")
                lose_game()

            last_number = sequence[-1]

            if last_number == 21:
                lose_game()

            # Computer prepares next move
            near = nearest_multiple_of_4(last_number)
            comp_count = near - last_number
            if comp_count == 4:
                comp_count = 3  # Avoid choosing 0

        print("\nCONGRATULATIONS! YOU WON!")
        sys.exit(0)

    else:
        print("Invalid choice! Please enter F or S.")

# Entry point of the program
while True:
    print("\n--- 21 Number Game ---")
    print("Player 2 is the Computer.")
    print("Do you want to play the game? (Yes / No)")
    answer = input("> ").strip().lower()

    if answer == "yes":
        play_game()
    elif answer == "no":
        print("Do you want to quit the game? (yes / no)")
        quit_answer = input("> ").strip().lower()
        if quit_answer == "yes":
            print("Quitting the game...")
            break
        elif quit_answer == "no":
            print("Continuing...")
        else:
            print("Invalid choice.")
    else:
        print("Invalid input. Please enter Yes or No.")
