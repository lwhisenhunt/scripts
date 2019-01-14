# import random
import os
from random import randint
def affirmation():
    # num=random.randint(0,9)
    rand=randint(0,9)
    affirmations= [
        "You are smart",
        "You are tall",
        "You will make today happen",
        "Make today great",
        "Today will be sunny",
        "Be Happy",
        "Don't worry",
        "Be Encouraging",
        "Set Goals",
        "Be your Best",
        "Don't spill your sprite"
    ]
    print(affirmations[rand])
    os.system("say '{}'".format(affirmations[rand]))
# affirmation()

def word_of_the_day():
    random=randint(0,4)
    words= [
        "today",
        "tomorrow",
        "tonight",
        "next year",
        "in one second",
    ]
    print(words[random])
    os.system("say '{}'".format(words[random]))
# word_of_the_day()

def run_both():
    word_of_the_day()
    affirmation()
