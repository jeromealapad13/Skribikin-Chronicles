import world, pickle
from classes import Knight
from sys import exit

def play():
    world.loadTiles()
    player = Knight("KingTako")
    room = world.tileExists(player.locationX, player.locationY)
    print(room.introText())
    while player.hp > 0:
        room = world.tileExists(player.locationX, player.locationY)
        room.modifyPlayer(player)
        print("Choose an action: \n")
        availableActions = room.availableActions()
        for action in availableActions:
            print(action)
        actionInput = input("\nAction: ")
        print()
        for action in availableActions:
            if actionInput == action.hotkey:
                player.doAction(action, **action.kwargs)
                break

def loadFile():
    with open("savefile", "rb") as f:
        data = pickle.load(f)
    world.loadedFileTiles(data.locationX, data.locationY)
    player = data
    room = world.tileExists(player.locationX, player.locationY)
    print(room.introText())
    while player.hp > 0:
        room = world.tileExists(player.locationX, player.locationY)
        room.modifyPlayer(player)
        if player.hp > 0:
            print("Choose an action: \n")
            availableActions = room.availableActions()
            for action in availableActions:
                print(action)
            actionInput = input("\nAction > ")
            print()
            for action in availableActions:
                if actionInput == action.hotkey:
                    player.doAction(action, **action.kwargs)
                    break
        else:
            print("You have died.")
            break

print("S = START\nL = LOAD\nX = QUIT\n")
choice = input("Input > ")
if choice.lower() == "s":
    play()
elif choice.lower() == "l":
    loadFile()
elif choice.lower() == "x":
    exit()