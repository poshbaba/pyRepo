#Prints bill for Rollercoaster ride based on Age and Height

Bill = 0
height = int(input("How tall are you in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")

    age = int(input("How old are you? "))
    if age <= 12:
        Bill = 5
        print("Child tickets are $12")
    elif age <= 18:
        Bill = 15
        print("Youth tickects are $15")
    elif age >= 30 and age <= 40:
        print("You get a free ride on US!")
    else:
        print("Adults tickets are $20")
        Bill = 20
    Response = input("Do you want a photo? Type Y for Yes and N for No  ")
    if Response == "Y":
        Bill += 3
        print(f"Your final bill is ${Bill}")
    else:
        print(f"Your final bill is ${Bill}")

else:
    print("You are too short to ride the rollercoaster")

