# import exit function from Python's system
from sys import exit


def dead():
    exit()

def game_start():
# opening scene
    print("You awaken lying on the ground deep in the jungle...")
    print("You are surrounded by dense foliage...")
    print("You hear a stream...")
    print("You see a snake dangling from a limb above you...")
    # asks user to choose an action
    print("""
What do you do?
- Stand up.
- Remain staring.
""")
    choice = input('> ')

    if choice == "Stand up.":
        print("""
    What do you do?
    - Look around.
    - Back up a few steps.
    """)
    else:
        print("The snake falls on you and bites you...")
        print("You feel your muscles begin to lock and your throat tighten as you breathe your last breath...")
        print("You are dead...")
        dead()

game_start()
