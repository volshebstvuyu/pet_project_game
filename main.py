import random

data = ""
hero_x = 5
hero_y = 5
life = int(data[0])
bag = []
location = "back_yard"  # Don`t forget replace to 'room'


def get_bag():
    for ids, inv in enumerate(bag):
        print(f'{ids + 1}) {inv}')


def level_room():
    global location
    global hero_x
    global hero_y
    global life
    global bag

    run = True
    apple_x = 7
    apple_y = 7
    key_x = 5
    key_y = 5
    door_x = 10
    door_y = 10
    door_key = False
    apple = True

    while run:
        print(f"x {hero_x} y {hero_y} life {life}")

        if hero_x == door_x and hero_y == door_y and "key" not in bag:
            print("You need the key to open the door, go back on x = 5, y = 5")

        elif hero_x == door_x and hero_y == door_y and "key" in bag:
            print("To go through the door using the key,type open")

        if hero_x == key_x and hero_y == key_y and not door_key and "key" not in bag:
            print("Type take to collect the key")

        if hero_x == apple_x and hero_y == apple_y and apple:
            print("Type eat")

        if hero_x == apple_x and hero_y == apple_y and not apple:
            print("Something was there...")

        if life < 1:
            location = "exit"
            run = False
            print("You are dead")

        cmd = input()

        if cmd == "q":
            location = "exit"
            run = False
            print("You've quite the game")

        elif cmd == "w":
            if hero_y < 10:
                hero_y += 1
            else:
                print("You've crushed with a wall")
                life -= 1

        elif cmd == "s":
            if hero_y > 1:
                hero_y -= 1
            else:
                print("You've crushed with a wall")
                life -= 1

        elif cmd == "d":
            if hero_x < 10:
                hero_x += 1
            else:
                print("You've crushed with a wall")
                life -= 1

        elif cmd == "a":
            if hero_x > 1:
                hero_x -= 1
            else:
                print("You've crushed with a wall")
                life -= 1

        elif cmd == "eat":
            if hero_x == apple_x and hero_y == apple_y and apple:
                life += 1
                apple = False

        elif cmd == "take" and hero_x == key_x and hero_y == key_y and not door_key:
            door_key = True
            bag.append("key")
            print("You've got the key")

        elif cmd == "bag":
            if len(bag) == 0:
                print("Bag is empty")
            else:
                get_bag()

        elif cmd == "open" and hero_x == door_x and hero_y == door_y and "key" in bag:
            print("You're on the next level")
            door_key = False
            # bag.remove("key")
            run = False
            location = "back_yard"


def level_back_yard():
    global location
    global hero_x
    global hero_y
    global life
    global bag

    run_back_yard = True
    door_x = 10
    door_y = 10
    hole_x = 10
    hole_y = 5
    car_x = 5
    car_y = 5
    apple_x = 1
    apple_y = 1
    key_x = 7
    key_y = 3
    hero_x = 7
    hero_y = 3
    key = False

    while run_back_yard:
        print(f"x {hero_x} y {hero_y} on back_yard life {life}")

        if life < 1:
            location = "exit"
            run_back_yard = False
            print("You are dead")

        if hero_x == hole_x and hero_y == hole_y and "tool" not in bag:
            print("There's a hole in the fence. I need some tool to break it.\n "
                  "Try to look in the car on x5 y5")

        elif hero_x == hole_x and hero_y == hole_y and "tool" in bag:
            print("Type break to go through the fence")

        if hero_x == apple_x and hero_y == apple_y and "apple" not in bag:
            print("Take an apple")

        if hero_x == key_x and hero_y == key_y and not key and "car_key" not in bag:
            print("Type take to collect the key")

        if hero_x == car_x and hero_y == car_y and not key:
            print("I forgot the key on x7 y3")

        elif hero_x == car_x and hero_y == car_y and key and "car_key" in bag:
            print("To look in the car for some tool,type open")

        if hero_x == door_x and hero_y == door_y:
            print("Type open to go back inside the room")

        cmd = input()

        if cmd == "q":
            location = "exit"
            run_back_yard = False
            print("You've quite the game")

        elif cmd == "w":
            if hero_y < 10:
                hero_y += 1
            else:
                print("You've crushed with a wall")
                life -= 1

        elif cmd == "s":
            if hero_y > 1:
                hero_y -= 1
            else:
                print("Be careful of bushes")

        elif cmd == "d":
            if hero_x < 10:
                hero_x += 1
            else:
                print(
                    "There's a fence, but I see s hole in it. We can use some tool "
                    "to break it open, maybe we should look in the car")

        elif cmd == "a":
            if hero_x > 1:
                hero_x -= 1
            else:
                print("Be careful of bushes")

        elif cmd == "take":  # and hero_x == apple_x and hero_y == apple_y and "apple" not in bag:
            if hero_x == apple_x and hero_y == apple_y and "apple" not in bag:
                bag.append("apple")
                print("You've got an apple")
            if hero_x == key_x and hero_y == key_y and not key:
                bag.append("car_key")
                key = True
                print("You've got the key")

        elif cmd == "eat":
            if "apple" in bag:
                life += 1
                bag.remove("apple")
            else:
                print(bag)

        # elif cmd == "take" and hero_x == key_x and hero_y == key_y and not key:
        #     bag.append("key")
        #     key = True
        #     print("You've got the key")

        elif cmd == "open":  # and hero_x == car_x and hero_y == car_y and key:
            if hero_x == car_x and hero_y == car_y and key:
                print("I see a big tool! We can use it, type take to collect it")
                # bag.remove("key")
                bag.append("tool")
                print("I've got the tool to break the fence")
            if hero_x == door_x and hero_y == door_y:
                run_back_yard = False
                # door = True
                # door_key = True
                # bag.append("key")
                location = "room"

        elif cmd == "bag":
            if len(bag) == 0:
                print("Bag is empty")
            else:
                get_bag()

        # elif cmd == "open" and hero_x == door_x and hero_y == door_y:  # and "key" in bag:
        #     run_back_yard = False
        #     # door = True
        #     door_key = True
        #     bag.append("key")
        #     location = "room"

        elif cmd == "break" and hero_x == hole_x and hero_y == hole_y and "tool" in bag:
            run_back_yard = False
            bag.clear()
            # location = "exit"
            # run = True
            print("You're on the next level")

def level_closed_yard():
    global location
    global hero_x
    global hero_y
    global life
    global bag

    run_closed_yard = True
    door_x = 3
    door_y = 2
    hole_x = 1
    hole_y = 1

    while run_closed_yard:
     print(f"x {hero_x} y {hero_y} on closed_yard life {life}")

    if hero_x == door_x and hero_y == door_y:
        print("There's a code lock on the door, to open it type letter subsequence  ")

    cmd = input()

    if cmd == "q":
        location = "exit"
        run = False
        print("You've quite the game")

    elif cmd == "w":
        if hero_y < 3:
            hero_y += 1
        else:
            print("You've crushed with a wall")
            life -= 1

    elif cmd == "s":
        if hero_y > 1:
            hero_y -= 1
        else:
            print("You've crushed with a wall")
            life -= 1

    elif cmd == "d":
        if hero_x < 3:
            hero_x += 1
        else:
            print("You've crushed with a wall")
            life -= 1

    elif cmd == "a":
        if hero_x > 1:
            hero_x -= 1
        else:
            print("You've crushed with a wall")
            life -= 1


while True:
    if location == "room":
        level_room()
    elif location == "back_yard":
        level_back_yard()
    elif location == "closed_yard":
        level_closed_yard()
    elif location == "exit":
        break
