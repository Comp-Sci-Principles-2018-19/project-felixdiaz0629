#Special thanks to Bowen and Malcolm

from adventurelib import *
import random

class Player:
    """this represents the player"""
    def __init__(self,gold=0,health=100):
        self.gold=gold
        self.health=health
Room.items = Bag()
player=Player()


current_room = starting_room = Room("""
You are in a dark room.
""")

valley = starting_room.north = Room("""
You are in a beautiful valley.
""")

playground = starting_room.east = Room("""
you are in the playground,
""")

riverbank = playground.north = valley.east = Room("""
You take a break and drink some coffee. You need to find a way to across the river,
""")

forest = riverbank.east = Room("""
you lumber some trees to make a wood bridge
""")

magic_forest = valley.north = Room("""
You are in a enchanted forest where magic grows wildly.
""")

monsterroom = valley.west = Room("""
you are facing a monster now and you have to defeat him in order to get the information of the right way,
""")

gaschamber = monsterroom.north = Room("""
you need to take a gasmask or you will die
""")

bombroom = gaschamber.east = Room("""
you need to care about bombs which are hidden underground
""")

dancingroom = gaschamber.east = Room("""
you can dance and relax my friend
""")

magicforest = dancingroom.east = Room("""
here is your destination, give me the key or not
""")
junglebranch=starting_room.south=Room("""
You are in a jungle. You find a knife and monsters.""")

another_magic_forest = valley.north = Room("""
You are in a enchanted forest where magic grows wildly.""")

mallet = Item('rusty mallet', 'mallet')
valley.items = Bag({mallet, })
basketball = Item("basketball", "ball")
playground.items = Bag({basketball, })
key = Item('golden key', 'key')
gasmask = Item('gasmask', 'key')

# monsterroom.items = Bag({key})
inventory = Bag()


@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        current_room = room
        say('You go %s.' % direction)
        look()
        if room == magic_forest:
            set_context('magic_aura')
        elif room == monsterroom:
            say("you want to fight or run?")
            choice = input("fight or run")
            if choice == "fight":
                say("you defeat the monster and he drops a key")
                monsterroom.items = Bag({key})
            else:
                say("you are defeated and you start again")
                current_room = starting_room
        elif room == gaschamber:
            say("you want to take gasmask or go?")
            choice = input("take or go")
            if choice == "take":
                say("you are safe now and you can move to the next room")
                gaschamber.items = Bag({gasmask})
            else:
                say(" you are killed by toxic gas and you start again")
                current_room = starting_room
        elif room == magicforest:
            say("you give the key or not?")
            choice = input("give or not")
            if choice == "give":
                say("you give a key and now you have freedom")
                magicforest.items = Bag({key})
            else:
                say("you are killed by the guard in magic forest since you refuse to give a key. you such a trash")
                current_room = starting_room


@when('take ITEM')
def take(item):
    obj = current_room.items.take(item)
    if obj:
        say('You pick up the %s.' % obj)
        inventory.add(obj)
    else:
        say('There is no %s here.' % item)


@when('drop THING')
def drop(thing):
    obj = inventory.take(thing)
    if not obj:
        say('You do not have a %s.' % thing)
    else:
        say('You drop the %s.' % obj)
        current_room.items.add(obj)


@when('look')
def look():
    say(current_room)
    if current_room.items:
        for i in current_room.items:
            say('A %s is here.' % i)


@when('inventory')
def show_inventory():
    say('You have:')
    for thing in inventory:
        say(thing)


@when('cast', context='magic_aura', magic=None)
def cast(magic):
    print(magic)
    if magic == None:
        say("Which magic you would like to spell?")
    elif magic == "invisible":
        say("you are invisible, noone can see you.")


look()
start()