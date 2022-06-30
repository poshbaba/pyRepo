import random

#Head or Tail
a = random.randint(1,2)
if a == 2:
    print("Head wins!")
else:
    print("Tail wins!")

#Who will pay the Bill? - Russian roulette1
names = input("List your names separated by a comma ")
names = names.split(",")
items = len(names)
choice = random.randint(0, items - 1)
manes = names[choice]
print(f"{manes} will pay the bills")

#Who will pay the Bill? - Russian roulette2
names = input("List your names separated by a comma ")
names = names.split(",")
final = random.choice(names)
print(f"{final} will pay the bills")