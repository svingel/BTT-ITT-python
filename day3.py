# Beetroot Academy - Intro To Tech - Week 4: Python
# Magdalena Kostrzewa

# Homework Day 3 Basic

friends = [
    ["Anita Reynolds", "anita.reynolds@example.com", 18, True],
    ["Carl Steward", "carl.steward@example.com", 21, False],
    ["John Doe", "john.doe@example.com", 45, True],
]

for friend in friends:
    print("%s, %d years old. Email: %s" % (friend[0], friend[2], friend[1]))

print("Best friends are: ")
for friend in friends:
    if friend[3] is True:
        print("%s" % friend[0])

# Homework Day 3 Advanced

phone_number = str(input('type in your phone number'))
if len(phone_number) != 10:
    print("Correct phone number must be 10 digits long")
elif phone_number.isdigit():
    print("Thank you!")
else:
    print("Please, input digits only")
