name = input("What is your name?: ")
age = int(input("What is your age?: "))
num = int(input("Give me a number: "))

hAge = 100 - age
hYear = 2020 + hAge

ans = name + " " + "will turn 100 years old in" + " " + str(hYear) + "!"

print("\n")
print("{}".format(ans))
print("\n")

for x in range(num):
    print("{}".format(ans))
