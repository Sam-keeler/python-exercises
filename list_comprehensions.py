fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Exercise 1 - rewrite the above example code using list comprehension syntax. 
# Make a variable named uppercased_fruits to hold the output of the list comprehension. 
# Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits = [x.upper() for x in fruits]
print(uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension 
# syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capital_fruits = [x.capitalize() for x in fruits]
print(capital_fruits)

# Exercise 3 - Use a list comprehension to make a variable named 
# fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel
vowels = 'aeiouAEIOU'
fruits_with_more_than_two_vowels = []
count = 0
for x in fruits:
    for char in x:
        if char in vowels:
            count = count + 1
    if count >= 2:
        fruits_with_more_than_two_vowels.append(x)
    count = 0
print(fruits_with_more_than_two_vowels)

# Exercise 4 - make a variable named fruits_with_only_two_vowels.
# The result should be ['mango', 'kiwi', 'strawberry']
vowels = 'aeiouAEIOU'
fruits_with_only_two_vowels = []
count = 0
for x in fruits:
    for char in x:
        if char in vowels:
            count = count + 1
    if count == 2:
        fruits_with_only_two_vowels.append(x)
    count = 0
print(fruits_with_only_two_vowels)

# Exercise 5 - make a list that contains each fruit with more than 5 characters
long_fruits = []
for x in fruits:
    if len(x) > 5:
        long_fruits.append(x)
print(long_fruits)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruits_of_five = []
for x in fruits:
    if len(x) == 5:
        fruits_of_five.append(x)
print(fruits_of_five)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruits_less_five = []
for x in fruits:
    if len(x) < 5:
        fruits_less_five.append(x)
print(fruits_less_five)