#  Prints Bill based on Pizza size, Pepperoni and Cheese
#Uses Nested if and elif statements
print("Welcome to PoshBaba Pizza!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
bill = 0
#Write your code below this line 👇
if size == "S":
  bill = 15
  print(f"Small size pizza is ${bill}")
  if add_pepperoni == "Y":
    bill += 2
    print(f"Bill for Small Pizza and Pepperoni is ${bill}")
  
elif size == "M":
  bill = 20
  print(f"Medium size pizza is ${bill}")
  if add_pepperoni == "Y":
    bill += 3
    print(f"Bill for Medium Pizza is ${bill}")    
else:
  bill = 25
  print(f"Big size pizza is ${bill}")
  if add_pepperoni == "Y":
    bill += 3
    print(f"Bill for Large Pizza is ${bill}")

if extra_cheese == "Y":
  bill += 1
  print(f"Your total bill is ${bill}")




