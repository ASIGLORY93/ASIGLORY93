user_name = input("What is your name? ").strip().title()


# check if name is on database
if user_name in names_database:
    age = input("How old are you? ").strip()
    else
message = f"Your name does nor exist"

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