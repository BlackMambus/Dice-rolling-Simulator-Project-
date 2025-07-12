import random

def roll_dice(sides=6):
    return random.randint(1, sides)

def main():
    print("🎲 Welcome to the Dice Rolling Simulator!")
    sides = input("Enter number of sides on the die (default is 6): ")
    sides = int(sides) if sides.isdigit() and int(sides) > 1 else 6

    while True:
        input("\nPress Enter to roll the die...")
        result = roll_dice(sides)
        print(f"🎯 You rolled a {result}!")

        again = input("Roll again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing!")
            break

if __name__ == "__main__":
    main()


