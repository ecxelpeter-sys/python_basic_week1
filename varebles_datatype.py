"""Examples of variables, data types, and comparison operators."""

a = 25
b = 20
print("sum:", a + b)

if a == b:
	print("a is equal to b")
else:
	print("a is not equal to b")

if 20 <= a <= 30:
	print("a is qualified")

school = "MODEL"
if school == "MODEL" or school == "NHS":
	print("you are qualified")
else:
	print("you are not qualified")

name = "Paul"
if name != "Peter":
	print("Name is not Peter")

# Age and gender check for the store.
age = int(input("How old are you? "))
gender = input("What is your gender? (male/female) ").lower()

if gender not in ("male", "female"):
	print("Please enter a correct gender")
elif age >= 18:
	print("You are old enough to buy alcohol.")
else:
	print("You are not old enough to purchase alcohol.")