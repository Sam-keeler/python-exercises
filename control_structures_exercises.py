# prompt the user for a day of the week, print out whether 
# the day is Monday or not
day = input("Whay day is it: ")
if str(day).lower() == "monday":
    print("It is Monday")
else:
    print("It most certainly is not Monday")

# prompt the user for a day of the week, print out whether 
# the day is a weekday or a weekend
weekday = input("What day is it :")
if str(weekday).lower() == "saturday" or str(weekday).lower() == "sunday":
    print("WEEKEND BABY")
else:
    print("It's a weekday")

# create variables and make up values for
# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck.
# You get paid time and a half if you work more than 40 hours
rate = 20
hours = input("How many hours have you worked this week?")
if hours <= 40:
    paycheck = rate * hours
else:
    paycheck = (40 * rate) + ((hours - 40) * rate * 1.5)
print(paycheck)

# While
# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i,
#  then increment i by one.
i = 5
print(i)
while i <= 15:
    print(i)
    i = i + 1

# Create a while loop that will count by 2's starting with 0 and
# ending at 100. Follow each number with a new line.
# Create a while loop that starts at 2, and displays the number squared 
# on each line while the number is less than 1,000,000. 
x = 0
while x <= 100:
    print(x)
    x = x + 2

# Alter your loop to count backwards by 5's from 100 to -10.
x = 100
while x >= -10:
    print(x)
    x = x - 5

# Create a while loop that starts at 2, and displays the number squared 
# on each line while the number is less than 1,000,000. 
x = 2
while x <= 1000000:
    print(x)
    x = x**2

# Write a loop that uses print to create the output shown below.
# (100 down to 5 in increments of 5)
x = 100
while x <= 5:
    print(x)
    x = x-5

# Write some code that prompts the user for a number, then shows 
# a multiplication table up through 10 for that number.
number = input("Gimme a number we're doing math, loser: ")
for i in range(1, 11):
    print(str(number) + " " + "X" + " " + str(i) + " "
     + "=" + " " + str(int(number) * i))

# Create a for loop that uses print to create the output shown below.
# (Number starting from 1 with repeating values equal to the number)
for i in range(1, 10):
    print(i * str(i))

# Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if 
# they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd 
# numbers between 1 and 50, except for the number the user entered.
while true:
    odd_num = input("Give me an odd number between 0 and 50: ")
    if odd_num.isdigit() and int(odd_num) > 0 and int(odd_num) < 50 and int(odd_num) % 2 != 0:
        break
print("Number to skip is:" + " " + str(odd_num))
for i in range(1, 51, 2):
    if int(odd_num) != i:
        print("Here is an odd number:" + " " + str(i))
    else:
        print("Yikes! Skipping number" + " " + str(odd_num))



