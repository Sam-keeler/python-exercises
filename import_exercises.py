#Import and test 3 of the functions from your functions exercise file.
import function_exercises
function_exercises.get_letter_grade(88)
# Output: B

from function_exercises import twelveto24
twelveto24('6:38pm')
# Output 18:38

from function_exercises import cumulative_sum as qsum
qsum((1, 8, 17, 2))
# Output [1, 9, 26, 28]

# For the following exercises, read about and use the itertools module from the 
# standard library to help you solve the problem.

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
from itertools import permutations
len(list(permutations('ABC123')))
# Output 720

# How many different ways can you combine two of the letters from "abcd"?
from itertools import permutations
len(list(permutations('abcd', 2)))
# Output 12

# Save this file as profiles.json inside of your exercises directory. 
# Use the load function from the json module to open this file, it will 
# produce a list of dictionaries. Using this data, write some code that 
# calculates and outputs the following information:
import json

with open('profiles.json') as profiles:
    data = json.load(profiles)

# Total number of users
print(len(data))
# Output 19

# Number of active users
len([profile for profile in data if profile['isActive']])
# Output 9

# Number of inactive users
len([profile for profile in data if profile['isActive'] == False])
# Output 10

# Grand total of balances for all users
balances = [profile['balance'] for profile in data]
for i in range(0, len(balances)):
    balances[i] = balances[i].replace('$', '')
    balances[i] = balances[i].replace(',', '')
    balances[i] = float(balances[i])
print(sum(balances))

# Average balance per user
balances = [profile['balance'] for profile in data]
for i in range(0, len(balances)):
    balances[i] = balances[i].replace('$', '')
    balances[i] = balances[i].replace(',', '')
    balances[i] = float(balances[i])
print((sum(balances)/(len(balances))))

# User with the lowest balance
balances = [profile['balance'] for profile in data]
for i in range(0, len(balances)):
    balances[i] = balances[i].replace('$', '')
    balances[i] = balances[i].replace(',', '')
    balances[i] = float(balances[i])
ind = balances.index(min(balances))
print(data[ind]['name'])

# User with the highest balance
balances = [profile['balance'] for profile in data]
for i in range(0, len(balances)):
    balances[i] = balances[i].replace('$', '')
    balances[i] = balances[i].replace(',', '')
    balances[i] = float(balances[i])
ind = balances.index(max(balances))
print(data[ind]['name'])

# Most common favorite fruit
from collections import Counter
fruits = [profile['favoriteFruit'] for profile in data]
count = Counter(fruits)
print(list(count.keys())[0])

# Least most common favorite fruit
from collections import Counter
fruits = [profile['favoriteFruit'] for profile in data]
count = Counter(fruits)
print(list(count.keys())[-1])

# Total number of unread messages for all users
messages = [profile['greeting'] for profile in data]
for message in messages:
    for char in message:
        if char not in ('0123456789'):
            message = message.replace(char, '')
for i in range(0, len(messages)):
        messages[i] = int(messages[i])
print(messages)



