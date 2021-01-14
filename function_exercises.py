# Define a function named is_two. It should accept one input and return True
# if the passed input is either the number or the string 2, False otherwise.
def is_two(x):
    if int(x) == 2:
        return True
    else:
        return False

# Define a function named is_vowel. It should return True 
# if the passed string is a vowel, False otherwise.
def is_vowel(x):
    vowel = 'aeiou'
    if x.lower() in vowel:
        return True
    else:
        return False

# Define a function named is_consonant. It should return True if the 
# passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_continent(x):
    vowel = 'aeiou'
    if x.lower() not in vowel:
        return True
    else:
        return False

# Define a function that accepts a string that is a word. The function should capitalize 
# the first letter of the word if the word starts with a consonant.
def cap_them_cons(x):
    vowel = 'aeiou'
    if x.lower()[0] not in vowel:
        return x.capitalize()
    else:
        return x

# Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(x, y):
    return x * y

# Define a function named apply_discount. It should accept a original price, and a 
# discount percentage, and return the price after the discount is applied.
def apply_discount(o_price, percent):
    return (1 - (.01 * percent)) * o_price

# Define a function named handle_commas. It should accept a string that is 
# a number that contains commas in it as input, and return a number as output.
def handle_commas(x):
    x = x.replace(',', '')
    return x

# Define a function named get_letter_grade. It should accept a number 
# and return the letter grade associated with that number (A-F).
def get_letter_grade(x):
    if x >= 90:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    else:
        return 'F'

# Define a function named remove_vowels that accepts a string and returns a 
# string with all the vowels removed.
def remove_vowels(x):
    vowel = 'aeiou'
    for y in x:
        if y.lower() in vowel:
            x = x.replace(y, '')
    return x

# Define a function named normalize_name. It should accept a string and return a valid python 
# identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
def normalize_name(x):
    x = x.strip()
    x = x.lower()
    for y in x:
        if y not in ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '):
            x = x.replace(y, '')
        if y == ' ':
            x = x.replace(y, '_')
    return x

# Write a function named cumulative_sum that accepts a list of numbers and returns 
# a list that is the cumulative sum of the numbers in the list.
def cumulative_sum(x):
    




