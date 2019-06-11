from adventurelib import *
import random


class Player:
    """this represents the player"""

    def __init__(self, gold=0, health=100):
        self.gold = gold
        self.health = health


Room.items = Bag()
player = Player()
current_room = starting_room = Room("""
You are in a dark room.
""")

valley = starting_room.north = Room("""
You are in a beautiful valley.
""")

junglebranch = starting_room.south = Room("""
You are in a jungle. You find a knife and monsters.""")

magic_forest = valley.north = Room("""
You are in a enchanted forest where magic grows wildly.""")

mallet = Item('rusty mallet', 'mallet')
valley.items = Bag({mallet, })
sword = Item("sword", "weapons")
Axe = Item("axe", "weapon")
knife = Item("a shinny knife", "knife")
junglebranch.items = Bag({knife})
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
        else:
            set_context('default')
        if room == junglebranch:
            say("Do you fight the monster")


@when('take ITEM')
def take(item):
    obj = current_room.items.take(item)
    if obj:
        say('You pick up the %s.' % obj)
        inventory.add(obj)
    else:
        say('There is no %s here.' % item)


def take(sword):
    obj = magic_forest.sowrd.take(sword)


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
    if magic == None:
        say("Which magic you would like to spell?") = -]

        @when("fight")


def fight():
    global current_room
    rng = random.Random()
    coin = rng.randrange(1, 3)
    if coin == 1 and "knife" in inventory:
        say("You defeated the monster, he give you 100 gold and can now move on")
        player.gold = player.gold + 100
    else:
        say("You are dead and are sent back to the start. Remember to take the knife.")
        current_room.exit("north")


look()
start()