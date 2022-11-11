new=True

while new:
    num = int(input("enter the num = "))

    if num > 0:
        print("prositive number...")
    elif num == 0:
        print("zero number...")
    else:
        print("negative number....")

    choice = input("do you continue to press y/n = ")
    if choice == "y":
        new=True
    else:
        new=False
