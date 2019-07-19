# Let's do something fun.  It's not quite Game of Thrones, but whichever of your
# friends get the best result can claim the theoretical Iron Throne.  For today's
# challenge you'll create a script called game_of_sums.py.  It should do the
# following:
#
#     1.  Create a variable to hold the start time.
#     2.  Loop 10 times and prompt the user to answer a simple addition question
#         of two randomly generated numbers between 0 and 150.
#     3.  The user should have to continue guessing a sum until he/she gets it right.
#     4.  When all questions have been answered your program should create a
#         second variable with the end time.
#     5.  Calculate how much time has passed between starting and ending.
#     6.  If the user took more than 120 seconds, you should respond "Hmmm. that
#         took a bit long.  Better luck next time."
#     7.  If the user took between 60 and 120 seconds, you should respond "Pretty
#         good.  But maybe you can do better."
#     8.  If the user took between 30 and 60 seconds, you should respond "Excellent
#         job.  You answered a least every 5 seconds."
#     9.  If the user took 30 seconds or less, you should respond "Extremely
#         impressive!  You answered in less than 30 seconds."
#
# Here's an example of how it should run:
#
#     >>> jgreen$ python3 answer.24.game_of_sums.py
#     What is 17 + 111: 128
#     What is 30 + 39: 69
#     What is 145 + 69: 254
#     Incorrect.  try again: 264
#     Incorrect.  try again: 204
#     Incorrect.  try again: 214
#     What is 61 + 16: 77
#     What is 132 + 40: 172
#     What is 104 + 137: 241
#     What is 95 + 33: 128
#     What is 30 + 60: 90
#     What is 16 + 17: 33
#     What is 52 + 32: 84
#     It took you 70.643833 seconds to answer these questions.
#     Pretty good.  But maybe you can do better.
#
# May the best Dany or Jon win!
# Answers to today's questions will be sent tomorrow.
# from datetime import datetime
# start_time = datetime
# print(start_time)
from random import randint
from datetime import datetime
import time
#
name = input('Hello, Welcome to Game of Sums!!  What is your name? ')
start_time = datetime.now()
print(start_time)
RANGE_OF_QUESTIONS = 10
for x in range(10):
    a = randint(1,RANGE_OF_QUESTIONS)
    b = randint(1,RANGE_OF_QUESTIONS)
    answer = (a+b)
    question = input('what is {} + {} '.format(a,b))
    question = int(question)
    if answer != question:
        print('Wrong answer, try again')
        question = input('what is {} + {} '.format(a,b))
    else:
        print('good job!!')

end_time = datetime.now()
print(end_time)

# %s only returns the seconds portion of the time.
# used the strftime function with %s to convert my datetime objects into seconds
# start_time = int(start_time.strftime('%s'))
# end_time = int(end_time.strftime('%s'))
# length = end_time - start_time
# print(length, 'seconds')
#subtracting datetime objects from each other, returns a timedelta object which allows you to use total.seconds method
length = end_time - start_time
print('Thanks for playing!!', name, 'your time was', length, 'seconds!!')
# from datetime import datetime, time


# #this is current time as datetime object
# current = datetime.now()
# #need to parse in a date to create a datetime
# future = datetime.strptime('07/19/2019 12:00:00.00', '%m/%d/%Y %H:%M:%S.%f')
#
# difference = future - current
# print(difference.total_seconds(), 'seconds')
# # print(difference.days(), 'days')








# Here are answers to yesterday's code challenge.  Note, there may be multiple ways demonstrated in answers below

## This script uses:
#    if statements
#    datetime.now()
#    random.randint()
#    timedelta.total_seconds()
#    while loops
#    string.strip()
#    string.format()

# # Import some libraries
# from datetime import datetime
# from random import randint
#
# # Set start_time to current time
# start_time = datetime.now()
#
# # Initialize a counter for our loop
# count=1
# # We'll stop when our count has hit 10
# while count <= 10:
#     # Set two random numbers between 0 and 150.  Then find their sum
#     num1 = randint(0,150)
#     num2 = randint(0,150)
#     answer = int(num1) + int(num2)
#
#     # Ask the user to give an answer for the sum of num1 and num2
#     response = input("What is {} + {}: ".format(num1, num2))
#     # Strip white spaces from beginning and end
#     response = response.strip()
#
#     # Check to see if the int() version of our response equals the answered
#     # If not, request that they give an answer agina.
#     while int(response) != answer:
#         response = input("Incorrect.  try again: ")
#     # Increment our count.
#     count += 1
#
# # Set our end time to the new current time
# end_time = datetime.now()
# # Get the difference of the start and end times.  This subtraction returns
# # a datetime.timedelta object which has a .total_seconds() function
# duration = end_time - start_time
#
# print("It took you {} seconds to answer these questions.".format(duration.total_seconds()))
# if duration.total_seconds() > 120:
#     print("Hmmm. That took a bit long.  Better luck next time.")
# elif duration.total_seconds() > 60:
#     print("Pretty good.  But maybe you can do better.")
# elif duration.total_seconds() > 30:
#     print("Excellent job.  You answered at least every 5 seconds.")
# else:
#     print("Extremely impressive!  You answered in less than 30 seconds.")
