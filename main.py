from madlib1 import story1
from madlib2 import story2
from madlib3 import story3
from title import title
import os
import time

def main():  # sourcery skip: extract-duplicate-method
    title()

    print('''
    **If you want to exit, press CTRL+C

    (1) Cold November Day
    (2) The Magic Computers
    (3) Kronos and his Throne
    ''')

    valid = True
    while valid:
        try:
            choose = input("    Choose a story (1-3): ")
            choose = int(choose)

            if choose > 3:
                print("    ***Not a valid choice, please try again!***")

            elif choose == 1:
                os.system("cls")
                print("Loading story...")
                time.sleep(2)
                os.system("cls")
                story1()
                time.sleep(2)
                play_again = input("\nWanna play again? (yes/no): ")
                if play_again in ["yes", "y", "yeah"]:

                    main()
                else:
                    os.system("cls")
                    valid = False

            elif choose == 2:
                os.system("cls")
                print("Loading story...")
                time.sleep(2)
                os.system("cls")
                story2()
                time.sleep(2)
                play_again = input("\nWanna play again? (yes/no): ")
                if play_again in ["yes", "y", "yeah"]:
                    main()
                else:
                    os.system("cls")
                    valid = False

            elif choose == 3:
                os.system("cls")
                print("Loading story...")
                time.sleep(2)
                os.system("cls")
                story3()
                time.sleep(2)
                play_again = input("\nWanna play again? (yes/no): ")
                if play_again in ["yes", "y", "yeah"]:
                    main()
                else:
                    os.system("cls")
                    valid = False

        except ValueError:
            print("    ***Not a valid choice, please try again!***")
            valid = True
        
        except KeyboardInterrupt:
            os.system("cls")
            print("KeyboardInterrupt exception caught, exiting...")
            time.sleep(1)
            quit()



if __name__ == '__main__':
    main()