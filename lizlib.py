# import random
import os
from random import randint
def affirmation():
    # num=random.randint(0,9)
    num=randint(0,9)
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
        "Be your Best"
    ]
    print(affirmations[num])
    os.system("say '{}'".format(affirmations[num]))
# affirmation()

def word_of_the_day():
    word=randint(0,4)
    words= [
        "happy",
        "today",
        "sunshine",
        "video",
        "turner"
    ]
    print(words[word])
# word_of_the_day()

def run_both():
    word_of_the_day()
    affirmation()
