# Beetroot Academy - Intro To Tech - Week 4: Python
# Magdalena Kostrzewa

# Homework Day 2 Basic

friend_1_name = "Anita Reynolds"
friend_1_age = 18
friend_1_email = "anita.reynolds@example.com"
friend_1_the_best = True

friend_2_name = "John Doe"
friend_2_email = "john.doe@example.com"
friend_2_age = 45
friend_2_the_best = True

print("%s, %d years old. Email: %s" % (friend_2_name, friend_2_age, friend_2_email))

# Homework Day 2 Advanced

from datetime import datetime
day = (datetime.today().strftime('%A'))
name = 'Magdalena'
print(f'Good day, {name}! {day} is a perfect day to learn some Python.')
