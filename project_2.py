#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction] - north, south, east, west.
  get [item] - Get the item.
  teleport [room] - To go to a new room.
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + str(rooms[currentRoom]['item']))
  print("---------------------------")
  
#an inventory, which is initially empty
inventory = []

# added dictionary for item descriptions
desc = {
          'key': 'You have the key to the fortress!',
          'potion': 'You just got the magic potion!',
          'pot': 'You have the pot use it wisely!',
          'cookie': 'You have the cookie, Yum!',
          'staff': 'You have the magic staff!',
          'knife': 'Man that knife is sharp!',
          'cake' : 'I hope that cake tastes good as the cookie!'
}

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
# added multiple items to the rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster'
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : ['potion', 'staff'],
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'item'  : ['pot', 'knife']
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'west'  : 'Hall',
                  'item' : ['cookie', 'cake']
            },
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  if move[0] == 'teleport':
    if move[1].capitalize() in rooms:
      currentRoom = move[1].capitalize()
      print("You are now in", move[1].capitalize())
    else:
      print("Sorry that room doesn't exist")
      # Teleport method for going to different rooms
      
  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!', desc[move[1]])
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break
  elif currentRoom == 'Pantry' and 'key' in inventory and 'cookie' in inventory:
    print('You escaped the house with the ultra rare key and the cookie so eat up... YOU WIN!')
    break
  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
