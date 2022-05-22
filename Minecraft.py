def main():
    cows = input("Enter how many adult cows you have: ")

    while not cows.isdigit() or int(cows) < 1:
        print("Please, enter an integer more than 1.")
        cows = input("Enter how many adult cows you have: ")

    requiredCows = input("Enter the total cows you need: ")

    while not requiredCows.isdigit() or int(requiredCows) < int(cows):
        print("Please, enter an integer more than the cows you have.")
        requiredCows = input("Enter the total cows you need: ")

    cowsDetails(int(requiredCows), int(cows))


def cowsDetails(requiredCows, cows):
    # initializing variables.
    TO_GROW_UP = 2  # two days for babies to become adults.
    DAY_IN_REAL = 10  # 10 min in real life = one day in minecraft.
    requiredDays = 0
    requiredWheat = 0
    babies = []

    while cows + sum(babies) < requiredCows:

        # for babies when they become adults.
        if requiredDays != 0 and requiredDays % 2 == 0:
            cows += babies[0]
            babies.pop(0)

        # calculating the wheat.
        if cows % 2 == 0:
            requiredWheat += cows
        else:
            requiredWheat += cows - 1

        babies.append(cows // 2)
        requiredDays += 1

    # Results.
    print(f"\n\nRequired days: {requiredDays} days")
    print(f"Total minutes in real life: {requiredDays * DAY_IN_REAL} mins")
    print(f"\nRequired wheat: {requiredWheat} wheat")
    print(f"\nTotal cows: {cows + sum(babies)} cows >> {cows} Adult cows and {sum(babies)} baby cows.\n")


main()