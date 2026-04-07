import random

options = ["🪨", "📄", "✂️"]
bot_choice = random.choice(options)

print("Welcome to Rock, Paper, Scissors! \n Please enter your choice with either 🪨, 📄, ✂️, or enter [q] to quit.")
choice = input("> ")

while True:
    print(f"My choice: {bot_choice}\n Your choice: {choice}")
    if choice == "🪨":
        if bot_choice == "🪨":
            print("It's a tie!")
            break
        elif bot_choice == "📄":
            print("You lost!")
            break
        elif bot_choice == "✂️":
            print("You win!")
            break
    elif choice == "📄":
        if bot_choice == "🪨":
            print("You win!")
            break
        elif bot_choice == "📄":
            print("It's a tie!")
            break
        elif bot_choice == "✂️":
            print("You lost!")
            break
    elif choice == "✂️":
        if bot_choice == "🪨":
            print("You lost!")
            break
        elif bot_choice == "📄":
            print("You win!")
            break
        elif bot_choice == "✂️":
            print("It's a tie!")
            break
    elif choice == "q":
        print("Goodbye!")
        break
    else:
        print("Please enter a valid choice!")




