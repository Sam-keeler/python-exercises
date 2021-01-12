# You have rented some movies for your kids: The little mermaid
# (for 3 days), Brother Bear (for 5 days, they love it), and Hercules 
# (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?
movie_days = [3, 5, 1]
movies = ['Little Mermaid', 'Brother Bear', 'Hercules']
price = sum(movie_days) * 3

# Suppose you're working as a contractor for 3 companies: Google, 
# Amazon and Facebook, they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 
# 4 hours for Amazon.
res_list = []
companies = ['Google', 'Amazon', 'Facebook']
rate =[400, 380, 350]
hours = [6, 4, 10]
for x in range(0, len(rate)):
    res_list.append(rate[x] * hours[x])
payment = sum(res_list)

# A student can be enrolled to a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.
is_conflicting = class_time in student_schedule
is_full = class_attendants >= class_capacity

# A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. Premium members do not need to buy a 
# specific amount of products.
discount = .8
for items in cart:
    if len(cart) >= 3 and offerdate < today() or premium_mem = True:
        price = sum(cart) * discount
    else:
        price = sum(cart)
return price

# Create a variable that holds a boolean value for each of 
# the following conditions:

# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace
username = 'codeup'
password = 'notastrongpassword'
min_length = len(password) >= 5
max_length = len(username) <= 20
is_same = username != password
has_spaces = username[0] != ' ' and username[-1] != ' ' and password[0] != ' ' and password[-1] != ' '

