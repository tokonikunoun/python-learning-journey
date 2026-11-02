# Week 1 completed coding exercises
# AI assistance: exercises, explanations, examples, hints, and feedback from an AI tutor.
# Teekay wrote the submitted solutions and corrected mistakes during the lesson.
# This file was assembled by AI from the final submitted code; indentation was
# normalized to four spaces. These are guided exercises, not independent projects.

# Exercise 01_printing
print("My name is Teekay")
print("I am learning Python")

# Exercise 02_string_variable
name = "Teekay"
print(name)

# Exercise 03_numeric_variable
study_hours = 2
print(study_hours)

# Exercise 04_update_variable
challenges_solved = 3
challenges_solved = challenges_solved + 2
print(challenges_solved)

# Exercise 05_f_string
challenges_solved = 5
print(f"I have solved {challenges_solved} challenges.")

# Exercise 06_two_variables
name = "Teekay"
study_hours = 2
print(f"{name} studied Python for {study_hours} hours today.")

# Exercise 07_calculation_in_f_string
hours_per_day = 2
days = 5
print(f"I studied for {hours_per_day * days} hours in total.")

# Exercise 08_combined_variables
name = "Teekay"
challenges_solved = 3
challenges_solved = challenges_solved + 2
print(f"{name} has solved {challenges_solved} challenges.")

# Exercise 09_if
challenges_solved = 5

if challenges_solved > 3:
    print("Target reached!")

# Exercise 10_if_else
challenges_solved = 2

if challenges_solved > 3:
    print("Target reached!")
else:
    print("Keep going!")

# Exercise 11_inclusive_boundary
challenges_solved = 3

if challenges_solved >= 3:
    print("Target reached!")
else:
    print("Keep going!")

# Exercise 12_study_goal
study_hours = 2

if study_hours >= 2:
    print("Daily goal reached!")
else:
    print("More practice needed.")

# Exercise 13_elif
challenges_solved = 4

if challenges_solved >= 5:
    print("Excellent Progress!")
elif 3 <= challenges_solved < 5:
    print("Good Progress!")
else:
    print("Keep practising!")

# Exercise 14_study_tracker
study_hours = 3

if study_hours >= 4:
    print("Excellent effort!")
elif 2 <= study_hours < 4:
    print("Daily goal achieved!")
else:
    print("Keep going!")

# Exercise 15_range
for number in range(1, 6):
    print(number)

# Exercise 16_loop_f_string
for number in range(1, 4):
    print(f"Challenge {number} completed!")

# Exercise 17_loop_condition
for number in range(1, 6):
    if number < 5:
        print(f"Working on challenge {number}.")
    else:
        print("All challenges completed!")

# Exercise 18_sum_one_to_five
total = 0

for number in range(1, 6):
    total = total + number

print(total)

# Exercise 19_sum_three_to_seven
total = 0

for number in range(3, 8):
    total = total + number

print(total)

# Exercise 20_conditional_sum
total = 0

for number in range(1, 7):
    if number > 3:
        total = number + total

print(total)

# Exercise 21_running_totals
total = 0

for number in range(1, 6):
    total = number + total

    print(total)
