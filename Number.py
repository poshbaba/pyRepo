#Give the sum of any two numbers

a = (input("Type any 2-digit number\n"))
b = int(a[0]) + int(a[1])
print(str(b) + " is Your answer")

#Checks if given number is even or odd

number = int(input("What number would you like to check for? "))
new = number % 2 

if new == 0:
    print(f"{number} is an even Number")

else: 
        print(f"{number} is an odd number")
