sword = 5
dog = 7
triforce = 11

current_capacity = 0


print("Hi! I can make a sword, dog, or triforce.")
balloon = input("Which balloon do you want? ")

while True:
    if balloon == "sword":
        print(f"Balloon: {balloon}")
        print(f"Capacity: {sword}")
        print(f"Current: {current_capacity}")
        choice = input(" [pump] air, [release] air, [tie] balloon> ")
        if choice == "pump":
                current_capacity += 3
                if current_capacity > sword:
                    print("POP!")
                    break
        if choice == "release":
            current_capacity -= 2
            if current_capacity >= 0:
                 current_capacity == 0
        if choice == "tie":
            print("Enjoy your balloon!")
            break

    if balloon == "dog":
        print(f"Balloon: {balloon}")
        print(f"Capacity: {dog}")
        print(f"Current: {current_capacity}")
        choice = input(" [pump] air, [release] air, [tie] balloon> ")
        if choice == "pump":
                current_capacity += 3
                if current_capacity > dog:
                    print("POP!")
                    break
        if choice == "release":
            current_capacity -= 2
            if current_capacity >= 0:
                current_capacity == 0
        if choice == "tie":
            print("Enjoy your balloon!")
            break
    if balloon == "triforce":
        print(f"Balloon: {balloon}")
        print(f"Capacity: {triforce}")
        print(f"Current: {current_capacity}")
        choice = input(" [pump] air, [release] air, [tie] balloon> ")
        if choice == "pump":
                current_capacity += 3
                if current_capacity > triforce:
                    print("POP!")
                    break
        if choice == "release":
            current_capacity -= 2
            if current_capacity >= 0:
                    current_capacity == 0
        if choice == "tie":
                print("Enjoy your balloon!")
                break


