#this is an mini RPG
#How do I make the game restart from here?
import sys
def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def startgame():
    print("Welcome to THRASHER")
    playername = input("What is your name, bro?")
    print (playername + ", What a cool name! I heard you are a strong warrior. I have a quest for you. In the Forbidden Forest, there are rumors of a portal. No one knows where it leads and those who enter do not return.")


    choice1 = input("Will you except this quest?")
    if playername == "Felix" and choice1 == "Yes":
        return"Ok lets get started!"
    elif choice1 == "No":
        print ("You Are Dead. Try Again?")  
        startgame()


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(testgame() == )

startgame()
test_suite()

choice2 = input("What will you do? Run or Fight?")
if choice2 == "Run":
    print("You try to run but aren't fast enough. You Are Dead. Try Again.")
    startgame()
    
elif choice2 == "Fight":
    print("You begin to enter you fighing stance.")


choice3 = input("What attack will you use? Stab , Fireball , Charge , or Heal?")
if choice3 == "Stab":
    print("You stab the goblin and deal 20 damage")
    print("You battle taking turns per attack and are about to take the final blow when the final boss appears to save his goblin and scare you with his power. He attacks you leaving you in CRITICAL condition. Then, he leaves.")
    print("You need to heal. There is a nearby village you walk to and you find a shop selling items. The man sees you and offers you a Max HP potion. He then asks you to go on a mission for him.")
elif choice3 == "Fireball":
    print("You attack the goblin with a fireball dealing 30 damage and use 15 mana points")
    print("You battle taking turns per attack and are about to take the final blow when the final boss appears to save his goblin and scare you with his power. He attacks you leaving you in CRITICAL condition. Then, he leaves.")
    print("You need to heal. There is a nearby village you walk to and you find a shop selling items. The man sees you and offers you a Max HP potion. He then asks you to go on a mission for him.")
elif choice3 == "Charge":
    print("You can not use charge. You already have full mana.")
elif choice3 == "Heal":
    print("You can not heal at this time. You have full HP.")


choice4 = input("Will you go on the mission?")
if choice4 == "Yes":
    print("Good! There is an ogre who lives in a cave south from here. If you bring me a tooth from the ogre, I will reward you with a new ability. Good luck!")
    print("You begin your journey towards the cave but are confronted by a group of thieves who try to take your items.")
elif choice4 == "No":
    print("Oh well I guess i have to find someone else now *the shop owner will remeber your choice") 


choice5 = input("What will you do? Run or Fight?")
if choice5 == "Run":
    print("You run back to the village but have not complete your mission")
elif choice5 == "Fight":
    print("The thieves overpower you and take your items")
    print("You walk back to the village, in shame")
