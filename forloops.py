#PRACTICE 1
#I provide a list of numbers I have named numbers.  Remember, a list is not an integer!!
#I create a variable named sum thats starts off as 0 and goes through the list
#Each time it runs each number in the list, its reassigned as a different variable before calculating the next numberself.

# numbers = [2,4,6,8,10] this is a list/dictionary
# sum = 0
# for number in numbers:  number is a stepper value
#     sum = sum + number       #not numbers because you can't add a list and an integer.  You have to use temp variables
#     print(sum)

#This produces 2, 6, 12, 20, 30

#PRACTICE 2
#Create an input from user to provide an integer, and then print the integer.
#Want to ensure user doesn't input anything but an integer.  I tried Except ValueError and that didnt work
#I tried say if answer < 0 but that doesnt work, just returned the normal error
# I tried "if int then, else" this returns the normal error message as well

# answer=input('Hello! Please pick a number ')
# try:
#     # range(answer)dont need this line, leave commented out
#     for hello in range(int(answer)):
#         print(hello)
# except ValueError:
#     print("please choose an integer")


#PRACTICE 3
# Its prints out the designated characted of each value, have to pick an indice that all values have.
# flowers=['rose', 'lily', 'peony', 'orchid']
# for plants in flowers:
#     try:
#         # printing the flowers list values in reverse
#         # print("pretty ",plants[5],plants[4],plants[3],plants[2],plants[1],plants[0])
#         plants=list(plants) #converted plants to a list
#         plants.reverse() #reversed each value in my plants list but its a list still
#         plants=''.join(plants) #I joined all the characters into a values so they arent separated by quotes
#         print(plants)
#     except IndexError:
#         print("pick a smaller word")

#PRACTICE 4
# import requests #imports API request library
# r= requests.get("http://athena.cp.vubble.it/#/events")
# print(r)


#PRACTICE 5- While loop EXERCISE
#ask a user to guess a number between 1-9
# import random #this is the random library, includes functions for generating random numbers
from random import randint #sepcify to use just the function for this library without having to specify the library each time, eg random.randint()
def make_integer(number):#I created this funtion so that everytime there is a reponse it checks if it can be made into an integer
    while True: #while statements have to be followed by T to execute. False will make it execute.
        try:
            int(number)
            break #break gets you out of an infinite loop
        except ValueError:
            number=input('please choose an integer ')
    return int(number)
secret=randint(1,2) #I want to tell my computer to choose a random integer between 1-10.  Have to call the library then the function for it to work.
response=input('Choose a number ') #this prompts the user to choose a number.  Purposely didnt instruct a range
quit= False #I want to define this globally, so set it outside of a code block- this is a good practice for other languages
while make_integer(response) != secret:#Until user guesses the right number, I want to keep prompting them to guess
    response=input('guess again ')
    # if make_integer(response) == secret:
    #     print('you win!, the answer is', secret)
    if response == 'quit':#changed this to quit so less likely to be chosen on accident
        response=secret
        quit= True
        print('quitter! the answer was', secret)
else:
    if quit != True:
        print('you win!, the answer is', secret)
