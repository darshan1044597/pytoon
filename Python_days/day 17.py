while True:
    print("u have two options, go left or right?")
    direction = input("> ")
    if direction == "left":
        print("u died LL")
        break
    elif direction == "right":
        print("u survived")
        continue
    else:
        print("go away")
        exit()
    print("game over")