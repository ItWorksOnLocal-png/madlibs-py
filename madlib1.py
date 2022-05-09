import os
import time


def story1():  # sourcery skip: extract-duplicate-method
    print("===Cold November Day===\n\n")
    story = '''It was a _________, cold November day. I woke up to the _________ smell of _________ roasting in the _________ downstairs.
I _________ down the stairs to see if I could help _________ the dinner. My mom said, "See if _________ needs a fresh _________."
So I carried a tray of glasses full of _________ into the _________ room. When I got there, I couldn't believe my _________!
There were _________  _________ on the _________!'''

    print("Let's see the story\n")
    print("=============================================================================================================================")
    print(story)
    print("=============================================================================================================================\n")
    print("You just have to complete the story, let's do this! Have fun!")
    os.system("pause")

    os.system("cls")
    print(story, "\n\n")
    print("Give me some words to complete the story\n")
    print("================================================")
    adj1 = input("Give me an adjective: ")
    adj2 = input("Give me an adjective: ")
    bird = input("Tell me a type of bird: ")
    room = input("Tell me a room in a house: ")
    verb = input("Give me a verb (past tense): ")
    verb1 = input("Give me a verb: ")
    relative = input("Tell me a relative's name: ")
    noun = input("Give me a noun: ")
    liquid = input("Tell me a liquid: ")
    verb2 = input("Give me a verb ending in -ing: ")
    body_part = input("Tell me a body part: ")
    plural_noun = input("Give me a plural noun: ")
    verb3 = input("Give me a verb ending in -ing: ")
    noun2 = input("Give me a noun: ")
    print("================================================")

    print("\nOk, that's all I need, let me rewrite it!")
    time.sleep(4)
    os.system("cls")
    print("Ok, here we go, let's see how's your story!\n")
    print("============================================================================================================")

    print(f'''It was a {adj1}, cold November day. I woke up to the {adj2} smell of {bird} roasting in the {room} downstairs.
I {verb} down the stairs to see if I could help {verb1} the dinner. My mom said, "See if {relative} needs a fresh {noun}."
So I carried a tray of glasses full of {liquid} into the {verb2}. room. When I got there, I couldn't believe my {body_part}!
There were {plural_noun}  {verb3} on the {noun2}!''')
    print("============================================================================================================")