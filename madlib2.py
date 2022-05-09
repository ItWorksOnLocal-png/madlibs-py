import os
import time

def story2():  # sourcery skip: extract-duplicate-method
    print("===The Magic Computers===\n\n")
    story = '''Today, every student has a computer small enough to fit into his ______.
He can solve any math problem by simply pushing the computer's little ______.
Computers can add, multiply, divide and ______. They can also ______ better than a human.
Some computers are ______. Others have a/an ______ screen that shows all kinds of ______ and ______ figures.'''

    print("Let's see the story\n")
    print("============================================================================================================")
    print(story)
    print("============================================================================================================\n")
    print("You just have to complete the story, let's do this! Have fun!")
    os.system("pause")
    
    os.system("cls")
    print(story, "\n\n")
    print("Give me some words to complete the story\n")
    print("================================================")
    noun = input("Give me a noun: ")
    plural_noun = input("Give me a plural noun: ")
    verb = input("Give me a verb (present tense): ")
    verb2 = input("Give me a verb (present tense): ")
    adj = input("Tell me an adjective: ")
    adj2 = input("Tell me an adjective: ")
    plural_noun2 = input("Tell me a plural noun: ")
    adj3 = input("Tell me an adjective: ")
    print("================================================")

    print("\nOk, that's all I need, let me rewrite it!")
    time.sleep(4)
    os.system("cls")
    print("Ok, here we go, let's see how's your story!\n")
    print("============================================================================================================")
    print(f'''Today, every student has a computer small enough to fit into his {noun}.
He can solve any math problem by simply pushing the computer's little {plural_noun}.
Computers can add, multiply, divide and {verb}. They can also {verb2} better than a human.
Some computers are {adj}. Others have a/an {adj2} screen that shows all kinds of {plural_noun2} and {adj3} figures.''')
    print("============================================================================================================")