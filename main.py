import random

def roll_dice(sides=6):
    return random.randint(1, sides)

def main():
    print("Welcome to the Dice Rolling Simulator!")

    while True:
        sides = int(input("Enter the number of sides for the dice (default is 6): ") or 6)

        if sides <= 0:
            print("Number of sides must be a positive integer.")
            continue

        roll = roll_dice(sides)
        print(f"You rolled a {roll}!")

        play_again = input("Roll again? (y/n): ").lower()
        if play_again != 'y':
            print("Exiting the Dice Rolling Simulator. Goodbye!")
            break

if __name__ == "__main__":
    main()
