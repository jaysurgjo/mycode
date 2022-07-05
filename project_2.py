#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''

The Game of Life!
========
Commands:

  go [direction] Type the direction north, south, east, west.
  get [item]

  go [1, 2, 3, 4] You can type in any of those numbers to get to a special room.
  get [item]

  go [5, 6, 7, 8] You can type in any of those numbers to get to a special room.
  get [item]
  
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You are currently in room ' + rooms[currentRoom] + ' and you have a '['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms

rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'Breakfast'
                },

            'Bathroom' : {
                  'north' : 'Hall',
                  'item'  : 'Toothbrush',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'Bagel',
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'item'  : 'Fresh Veggie'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
            }
         }

room_2 = {

        'Parking Lot': {
            '1': 'Emergency Exit',
            '2': 'Exit Ramp',
            '3' : 'Elevator',
            '4' : 'Stairs',
            'item'  : 'Parking Token'
            },

        'Subway': {
            '1': 'Train',
            '2': 'Stairs to the street',
            '3' : 'Ticket booth',
            '4' : 'Trip home',
            'item' : 'Train Pass'
            },

        'Gym': {
            '1': 'Leg Machine',
            '2': 'Bench',
            '3' : 'Cardio Bike',
            '4' : 'Shake stand',
            'item' : 'Free Gym Pass'
            }
        }

room_3 = {

        'Before Work': {
            '5': 'Gym',
            '6': 'Coffee',
            '7' : 'Bike to work',
            '8' : 'Take train to work',
            'item' : 'Day off from work'
            },

        'During work': {
            '5' : 'Go to IT',
            '6' : 'Meeting',
            '7'  : 'Lunch',
            '8'  : 'Go Home',
            'item' : 'Extended Lunch Break'
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

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
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

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
