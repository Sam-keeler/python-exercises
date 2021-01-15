# Define a function named is_two. It should accept one input and return True
# if the passed input is either the number or the string 2, False otherwise.
def is_two(x):
    #conditional to see if the integer form of what has been input is actually 2
    if int(x) == 2:  
    #if so, it returns True, if not, it returns False
        return True
    else:
        return False

# Define a function named is_vowel. It should return True 
# if the passed string is a vowel, False otherwise.
def is_vowel(x):
    #creating a list to identify vowels
    vowel = 'aeiou'
    #conditional seeing if the lowercase version of what was input is in our "vowel" variable
    if x.lower() in vowel:
    #if input is in "vowel" returns True, if not, it returns False
        return True
    else:
        return False

# Define a function named is_consonant. It should return True if the 
# passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(x):
    #creating a list to identify vowels
    vowel = 'aeiou'
    #conditional seeing if the lowercase version of what was input is in our "vowel" variable
    if x.lower() not in vowel:
    #if input is not in "vowel" returns True, if not, it returns False
        return True
    else:
        return False

# Define a function that accepts a string that is a word. The function should capitalize 
# the first letter of the word if the word starts with a consonant.
def cap_them_cons(x):
    #creating a list to identify vowels
    vowel = 'aeiou'
    #if input starts with a character that is not listed in "vowel", then capitalize that letter
    if x.lower()[0] not in vowel:
        return x.capitalize()
    #else just return the original input
    else:
        return x

# Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(tip_percent, bill_total):
    #if percentage is already given as a number between 0 and 1, simply multiplying the percentage
    #by the bill total will give you the tip amount
    return tip_percent * bill_total

# Define a function named apply_discount. It should accept a original price, and a 
# discount percentage, and return the price after the discount is applied.
def apply_discount(o_price, percent_off):
    #if percentage is given as an integer of the amount off the total price, then that integer
    #must be converted by dividing by 100. Then it must be subtracted from 1 so that instead of
    #displaying percent off, it displays the percentage of total price remaining. Then multiply by 
    #original price.
    return (1 - (.01 * percent_off)) * o_price

# Define a function named handle_commas. It should accept a string that is 
# a number that contains commas in it as input, and return a number as output.
def handle_commas(x):
    #if a comma is identified in the string, replaces that comma with nothing.
    x = x.replace(',', '')
    return x

# Define a function named get_letter_grade. It should accept a number 
# and return the letter grade associated with that number (A-F).
def get_letter_grade(grade):
    #creating bins to categorize each input, then diplays the bin that the input has been placed in
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

# Define a function named remove_vowels that accepts a string and returns a 
# string with all the vowels removed.
def remove_vowels(x):
    #creating a list to identify vowels
    vowel = 'aeiou'
    #looks through each individual character to determine if that character is contained in "vowel"
    for y in x:
    #if the character is contained in "vowel" then that character is replaced with nothing
        if y.lower() in vowel:
            x = x.replace(y, '')
    return x

# Define a function named normalize_name. It should accept a string and return a valid python 
# identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
def normalize_name(name):
    #removes white space at begginning and end of string
    name = name.strip()
    #lower cases any capital letters
    name = name.lower()
    for y in name:
    #conditional stating if any individual character is not a letter or space, replace it with nothing
        if y not in ('1234567890abcdefghijklmnopqrstuvwxyz '):
            name = name.replace(y, '')
    #conditional stating if a space is found (after stripping) to replace it with an underscore
        if y == ' ':
            name = name.replace(y, '_')
    return name

# Write a function named cumulative_sum that accepts a list of numbers and returns 
# a list that is the cumulative sum of the numbers in the list.
def cumulative_sum(x):
    #variables for computing and listing
    rnum = 0
    rlist = []
    #for loop starting at 0 and running up to the amount of elements in the input list
    for i in range(0, len(x)):
    #our variable "rnum" is a growing accumulation of each number in the list
        rnum = rnum + x[i]
    #variable "rlist" posts "rnum" for each iteration of the for loop
        rlist.append(rnum)
    return rlist

# thouroughly comment your code to explain your code

# Create a function named twelveto24. It should accept a string in the format 10:45am 
# or 4:30pm and return a string that is the representation of the time in a 24-hour format.
# Bonus write a function that does the opposite.
def twelveto24(time):
    adjuster = 0
    if time[-2] == 'p' and time[1] != '2':
        adjuster = 12
    if time[-2] == 'a' and time[1] == '2':
        adjuster = -12
    for y in time:
        if y not in ('1234567890:'):
            time = time.replace(y, '')
    time = time.split(':')
    for i in range(0, len(time)):
        time[i] = int(time[i])
    time[0] = time[0] + adjuster
    time = (str(time[0]) + ':' + str(time[1]))
    return time
        


