import os
import time

def story3():  # sourcery skip: extract-duplicate-method
    print("===Kronos and his Throne===\n\n")
    story = '''Kronos and Rhea ruled over the ______. ______ was in their power.
One day, when Rhea was about to have her first ______, her mother told Kronos that ______
of his children would become the ruler of the ______. Kronos was not ______. He decided if
his ______ were going to usurp his throne, he would ______ them first. So he did! Rhea was not
too ______ about this, and she managed to save her last ______, Zeus. He grew up in a ______,
hidden form his ______. But when he was old enough, he put on a ______ and made his father vomit
up all his brothers and ______. His plan worked! Zeus and his ______ were reunited.'''

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
    place = input("Tell me a place: ")
    noun = input("Give me a noun: ")
    noun2 = input("Give me a noun: ")
    number = input("Give me a number: ")
    noun3 = input("Give me a noun: ")
    emotion = input("Tell me an emotion: ")
    plural_noun = input("Give me a plural noun: ")
    verb = input("Give me a verb: ")
    emotion2 = input("Give me an emotion: ")
    noun4 = input("Give me a noun: ")
    place2 = input("Tell me a place: ")
    family_member = input("Tell me a family member: ")
    clothing = input("Tell me clothing article: ")
    family_member2 = input("Tell me a family member: ")
    family_member3 = input("Tell me a family member: ")
    print("================================================")

    print("\nOk, that's all I need, let me rewrite it!")
    time.sleep(4)
    os.system("cls")
    print("Ok, here we go, let's see how's your story!\n")
    print("============================================================================================================")
    print(f'''Kronos and Rhea ruled over the {place}. {noun} was in their power.
One day, when Rhea was about to have her first {noun2}, her mother told Kronos that {number}
of his children would become the ruler of the {noun3}. Kronos was not {emotion}. He decided if
his {plural_noun} were going to usurp his throne, he would {verb} them first. So he did! Rhea was not
too {emotion2} about this, and she managed to save her last {noun4}, Zeus. He grew up in a {place2},
hidden form his {family_member}. But when he was old enough, he put on a {clothing} and made his father vomit
up all his brothers and {family_member2}. His plan worked! Zeus and his {family_member3} were reunited.''')
    print("============================================================================================================")