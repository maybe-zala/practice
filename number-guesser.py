import random

turn = 0
points = 0

print("Welcome to Guess The Number!")
print("I'll think of a number, and you'll have to guess it!")
print("The closer your number is to mine, the more points you get! (# = your number)")
print(" # > 5 away from mine = 20 points")
print(" # > 10 away from mine = 10 points")
print(" # > 20 away from mine = 5 points")
print(" # > 30 away from mine = 1 points")
print("You have 6 rounds to try to get to 50 points!")

while True:
    if turn <= 5:
        mynum = random.randint(1,100)
        print("Please enter a number 1-100")
        usernum = int(input("> "))
        print("--------------------")
        print(f"My number: {mynum}")
        print(f"Your number: {usernum}")
        if abs(mynum - usernum) <= 5:
            print("You got 20 points!")
            points += 20
            turn += 1
            print(f"Points: {points}")
            print(f"Round: {turn}")
        elif abs(mynum - usernum) <= 10:
            print("You got 15 points!")
            points += 15
            turn += 1
            print(f"Points: {points}")
            print(f"Round: {turn}")
        elif abs(mynum - usernum) <= 15:
            print("You got 10 points!")
            points += 10
            turn += 1
            print(f"Points: {points}")
            print(f"Round: {turn}")
        elif abs(mynum - usernum) <= 20:
            print("You got 5 points!")
            points += 5
            turn += 1
            print(f"Points: {points}")
            print(f"Round: {turn}")

        elif abs(mynum - usernum) <= 30:
            print("You got 1 point!")
            points += 1
            turn += 1
            print(f"Points: {points}")
            print(f"Round: {turn}")
        else:
            print("Sorry! You didn't get any points!")
            turn += 1
            print(f"Points: {points}")
            print(f"Round: {turn}")       
    elif points < 50 and turn == 6:
        print("Sorry, you didn't win!")
        print("Would you like to play again? (Y/N)")
        choice = input("> ")
        if choice.lower() == "y":
            turn = 0
            points = 0
        elif choice == "n":
            break
    elif points >= 50 and turn == 6:
        print(f"Wow! You won! You got {points} points!")
        print("Would you like to play again? (Y/N)")
        choice = input("> ")
        if choice.lower() == "y":
            turn = 0
            points = 0
        elif choice.lower() == "n":
            break
    