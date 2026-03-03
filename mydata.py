name = input("What is your name? ").strip().title()
age = input("How old are you? ").strip()

# Validate age is a number
while not age.isdigit():
    age = input("Please enter a valid age (numbers only): ").strip()

age = int(age)

# Personalized message based on age
if age < 18:
    message = f"Welcome {name}! You're {age} years old. Enjoy your youth!"
elif age < 65:
    message = f"Welcome {name}! You're {age} years old. Great age to be!"
else:
    message = f"Welcome {name}! You're {age} years old. Age is just a number!"

print(message) 