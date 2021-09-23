# Beetroot Academy - Intro To Tech - Week 4: Python
# Magdalena Kostrzewa

# Homework Day 4 Basic

friends = [
    ["Anita Reynolds", "anita.reynolds@example.com", 18, True],
    ["Carl Steward", "carl.steward@example.com", 21, False],
    ["John Doe", "john.doe@example.com", 45, True],
]

choose_friends = str(input('Show all friends (a) or only the best friends (b)?'))

if choose_friends == "b":
    for friend in friends:
        if friend[3] is True:
            print("%s" % friend[0])
elif choose_friends == "a":
    for friend in friends:
        print("%s, %d years old. Email: %s" % (friend[0], friend[2], friend[1]))
else:
    print("You have to decide")

# Homework Day 4 Advanced

import random

print("Let's play a game. It's a number guessing game.")

x = random.randint(0, 10)

guess = int(input("Guess a number between 0 and 10: "))
if x == guess:
    print("Congratulations you did it!")
elif x > guess:
    print("You guessed too small!")
elif x < guess:
    print("You guessed too high!")
