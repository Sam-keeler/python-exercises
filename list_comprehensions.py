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

# Exercise 8 - Make a list containing the number of characters in each fruit. 
# Output would be [5, 4, 10, etc... ]
fruit_counts = []
for x in fruits:
    fruit_counts.append(len(x))
print(fruit_counts)

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only 
# the fruits that contain the letter "a"
fruits_with_a = []
count = 0
for x in fruits:
    for char in x:
        if char == 'a':
            count = count + 1
    if count > 0:
        fruits_with_a.append(x)
    count = 0
print(fruits_with_a)

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = []
for x in numbers:
    if x % 2 == 0:
        even_numbers.append(x)
print(even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = []
for x in numbers:
    if x % 2 != 0:
        odd_numbers.append(x)
print(odd_numbers)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
pos_numbers = []
for x in numbers:
    if x > 0:
        pos_numbers.append(x)
print(pos_numbers)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
neg_numbers = []
for x in numbers:
    if x < 0:
        neg_numbers.append(x)
print(neg_numbers)

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a 
# list of numbers with 2 or more numerals
big_numbers = []
for x in numbers:
    if x >= 10 or x <= -10:
        big_numbers.append(x)
print(big_numbers)

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with 
# each element squared. Output is [4, 9, 16, etc...]
sq_numbers = []
for x in numbers:
    sq_numbers.append(x**2)
print(sq_numbers)

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers 
# that are both odd and negative.
odd_neg_numbers = []
for x in numbers:
    if x < 0 and x % 2 != 0:
        odd_neg_numbers.append(x)
print(odd_neg_numbers)

# Exercise 17 - Make a variable named numbers_plus_5. In it, 
# return a list containing each number plus five. 
numbers_plus_5 = [x + 5 for x in numbers]
print(numbers_plus_5)

# BONUS Make a variable named "primes" that is a list containing the prime numbers 
# in the numbers list. *Hint* you may want to make or find a helper function that 
# determines if a given number is prime or not.
primes = []
for x in numbers:
    for i in range(2, x):
        if (x % i) == 0:
            primes.append(x)
print(primes)


