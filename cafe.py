print("Welcome to the Kitty Cafe!")

print("<=-Menu-=>")
print("> Meow de la Creme : $5.00 \n> Cat Cocoa Cake : $2.50 \n> Fish Food Taco : $7.29\n")

meow = 0
cat = 0
fish = 0

print("==================================\n")
while True:    
    order = input("What would you like?\nType 'done' when finished.\n> ")

    if order.lower() == "meow de la creme":
        meow += 1
        print("+1 Meow de la Creme added!")
    elif order.lower() == "cat cocoa cake":
        cat += 1
        print("+1 Cat Cocoa Cake added!")
    elif order.lower() == "fish food taco":
        fish += 1
        print("+1 Fish Food Taco added!")
    elif order.lower() == "done":
        print(f"Okay! Here is your order:\n {meow} Meow de la Cream : ${meow * 5.00}\n {cat} Cat Cocoa Cake : ${cat * 2.50}\n {fish} Fish Food Taco : ${fish * 7.29}")
        print(f"Your total is: ${meow * 5.00 + cat * 2.50 + fish * 7.29}")
        print("Thanks for your order! Have a good day!<3")
        break
    else:
        print("Sorry, that's not on the menu! Please choose something from the menu.")
    

