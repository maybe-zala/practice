
print("welcome to the pet boarding daycare! \n here you can trust your furry friend will be in great care while you get a break!")

room = 10

while True:
    print("what would you like to do?")
    print("1. drop off pet")
    print("2. pick up pet")
    print("3. exit")
    choice = input("> ")
    
    if choice == "1":
        print("you have choosen to drop off a pet.")
        if room <= 0:
            print("sorry, we don't have anymore room!")
            break
        else:
            print("please fill out some information about your pet:")
            name = input("What is your pets name?")
    elif choice == "2":
        break
    elif choice == "3":
        break
    else:
        print("that's not an option! please choose from the services listed.")

