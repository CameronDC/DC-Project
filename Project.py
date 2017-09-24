import pygame
import os
import ctypes
from time import sleep

pygame.init()

BLACK = (0, 0, 0)
RED = (255,0,0)               #Definign Colours
GREEN = (0, 255, 0)           #       v
BLUE = (0, 0, 255)            #       v
GRAY = ( 128, 128, 128)       #----------------
BROWN = (182, 155, 76)
LIGHTBLUE = (78, 104, 183)
WALLGREY = (93, 100, 51)
DOOR = (139,69,19)

bullet_hit_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group() # a list for all the sprites within the gaem
bullet_list = pygame.sprite.Group() # list for the bullets
imagelist = pygame.sprite.Group() # images which dont act as a wall list
enemylist = pygame.sprite.Group() # list for the enemies
walllist = pygame.sprite.Group() # list for the walls
playerlist = pygame.sprite.Group() #putting player in its own list
screen= pygame.display.set_mode((800, 800))#Screen size
keypress = pygame.key.get_pressed() 
rol = 0 #right or left setting to 0
uod = 0 # setting up or down to 0
score = 0
deaths = 99
myfont = pygame.font.SysFont("monospace", 30) # set font for the game
key = 0 # flag type attribute for if key has been collected

clock = pygame.time.Clock() #taking the pygame clock
RC = 1
roomnumber = 1
rooms = [0, 0]

#==============================================================================================
#--------------------------------------------Classes-------------------------------------------
#==============================================================================================

class Player(pygame.sprite.Sprite):
        def __init__(self, health, zero, damage):
            self.health = health        #Creating attributes of PLAYER --to be used later in game
            self.velocityx = zero       #                         v
            self.velocityy = zero       #                         v
            self.damage = damage
            self.roomchange = 1         #------------------------------------------------------
            super().__init__()
            self.image = pygame.image.load("N.png") #Load default image for player
            self.rect = self.image.get_rect()
            self.direction=100

        def facing(rol, uod):
            if keypress[pygame.K_RIGHT]:#Determining the durection of user (If Right AND....
                if keypress[pygame.K_UP]: #If Right and up 
                    player.image = pygame.image.load("NE.png") #Change player image to NE.png
                    player.direction=2
                elif keypress[pygame.K_DOWN]: #If right and down
                    player.image = pygame.image.load("SE.png") #Change player image to SE.png
                    player.direction=4
                else: #If it isnt up or down or left then it must be right which is East
                    player.image = pygame.image.load("E.png") #change player image to E.png
                    player.direction=3
            elif keypress[pygame.K_LEFT]: #Same system with the left side of the compass
                if keypress[pygame.K_UP]: #If left and up
                    player.image = pygame.image.load("NW.png") #Change player image to NW.png
                    player.direction=8
                elif keypress[pygame.K_DOWN]: #If left and down
                    player.image = pygame.image.load("SW.png") #Change player image to SW.png
                    player.direction=6
                else: #If it isnt up or down or right then it must be left which is West
                    player.image = pygame.image.load("W.png") #Change player image to W.png
                    player.direction=7
            elif keypress[pygame.K_DOWN]:                  #Is it north or south and changing
                player.image = pygame.image.load("S.png")  #              Image
                player.direction=5
            else:                                          #                v
                player.image = pygame.image.load("N.png")
                player.direction=1
                #---------------------------------
                
        def moving(): #Moving function consisting of direction + the determined velocity.
            player.rect.centerx = player.rect.centerx + player.velocityx
            player.rect.centery = player.rect.centery + player.velocityy


        def newroomchange():              # has the player left the boundaries of the map? 800 x 800 map, if so set room to change
            
            if player.rect.bottom <= 0:
                player.rect.bottom = 800
                rooms[1] = rooms[1] + 1
                player.roomchange = 1
            if player.rect.top >= 800:
                player.rect.top = 0
                rooms[1] = rooms[1] - 1
                player.roomchange = 1
            if player.rect.right <= 0:
                player.rect.right = 800
                rooms[0] = rooms[0] - 1
                player.roomchange = 1
            if player.rect.left >= 800:
                player.rect.left = 0
                rooms[0] = rooms[0] + 1
                player.roomchange = 1

        def update(self):
        # Update the player's position
        # Get the current mouse position. This returns the position
            pos = pygame.mouse.get_pos()

            

class Enemy(pygame.sprite.Sprite):
    def __init__(self):  # initial position
        super().__init__()
        self.image = pygame.image.load("enemy.png") #Load default image for enemy
        self.rect = self.image.get_rect()
    def move(speed): 
        # Movement along x direction
        if enemy.rect.centerx > player.rect.centerx:
            enemy.rect.centerx -= speed
        elif enemy.rect.centerx < player.rect.centerx:
            enemy.rect.centerx += speed
        # Movement along y direction
        if enemy.rect.centery < player.rect.centery:
            enemy.rect.centery += speed
        elif enemy.rect.centery > player.rect.centery:
            enemy.rect.centery -= speed

class Enemy2(pygame.sprite.Sprite):
    def __init__(self):  # initial position
        super().__init__()
        self.image = pygame.image.load("enemy.png") #Load default image for enemy No 2
        self.rect = self.image.get_rect()
    def move(speed): 
        # Movement along x direction
        if enemy2.rect.centerx > player.rect.centerx:
            enemy2.rect.centerx -= speed
        elif enemy2.rect.centerx < player.rect.centerx:
            enemy2.rect.centerx += speed
        # Movement along y direction
        if enemy2.rect.centery < player.rect.centery:
            enemy2.rect.centery += speed
        elif enemy2.rect.centery > player.rect.centery:
            enemy2.rect.centery -= speed  

        
class Wall(pygame.sprite.Sprite):                        #wall def, used for all wall in the game

    def __init__(self, width, height, colour ):
        self.colour = colour
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()

 #-------------------------------------------------------------------------------------
 # THE FOLLOWING DEFENITIONS ARE VARIABLES OF WALLS IN WHICH DIFFERENT IMAGES ARE USED
 #-------------------------------------------------------------------------------------

class Bench(pygame.sprite.Sprite):

    def __init__(self, width, height):
        
        super().__init__()
        self.image = pygame.image.load("bench1.png")
        self.rect = self.image.get_rect()

class FrontDesk(pygame.sprite.Sprite):

    def __init__(self, width, height):
        
        super().__init__()
        self.image = pygame.image.load("desk.png")
        self.rect = self.image.get_rect()

class Desk1(pygame.sprite.Sprite):

    def __init__(self, width, height):
        
        super().__init__()
        self.image = pygame.image.load("desk1.png")
        self.rect = self.image.get_rect()

class Sofa(pygame.sprite.Sprite):

    def __init__(self, width, height):
        
        super().__init__()
        self.image = pygame.image.load("sofa.png")
        self.rect = self.image.get_rect()

class Sofa1(pygame.sprite.Sprite):

    def __init__(self, width, height):
        
        super().__init__()
        self.image = pygame.image.load("sofa1.png")
        self.rect = self.image.get_rect()

class Image(pygame.sprite.Sprite):

    def __init__(self, width, height):
        
        super().__init__()
        self.image = pygame.image.load("download.png")
        self.rect = self.image.get_rect()

class Floor(pygame.sprite.Sprite):

    def __init__(self, width, height):
        
        super().__init__()
        self.image = pygame.image.load("floor.jpg")
        self.rect = self.image.get_rect()






class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self, player_x, player_y, player_direction):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([3, 3])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
        #self.direction=player_direction

    def move(self):
        if player.direction==1:
            self.rect.y-=8
        if player.direction==2:
            self.rect.x+=8
            self.rect.y-=8
        if player.direction==3:
            self.rect.x+=8
        if player.direction==4:
            self.rect.x+=8
            self.rect.y+=8
        if player.direction==5:
            self.rect.y+=8
        if player.direction==6:
            self.rect.x-=8
            self.rect.y+=8
        if player.direction==7:
            self.rect.x-=8
        if player.direction==8:
            self.rect.x-=8
            self.rect.y-=8

    ##def MakeBullet()
        
        







#Searchable locations:
class Box(pygame.sprite.Sprite):

    def __init__(self, width, height):
        
        super().__init__()
        self.image = pygame.image.load("box.png")
        self.rect = self.image.get_rect()
 

def Score():         # Pretty simply a score
        message_display(score)

def Deaths():         # Pretty simply a score
        message_display(deaths)
        
#image = Image()

enemy = Enemy()   #assingment
enemy2 = Enemy2()    #assingment
def newrooms():              #location of rooms called from Rooms() and locations of enemies
    if rooms == [-1,1]:
            roomnumber = 9
    if rooms[0] == 0 and rooms[1] == 1:
            print("triggered")
            roomnumber = 2
            enemy2 = Enemy2()
            enemy2.rect.centerx = 700
            enemy2.rect.centery = 700
            enemylist.add(enemy2)

    if rooms == [1,1]:
            roomnumber = 3
            enemy.rect.centerx = 100
            enemy.rect.centery = 100
            enemylist.add(enemy)
    if rooms == [-1,0]:
            roomnumber = 8
            enemy.rect.centerx = 100
            enemy.rect.centery = 100
            enemylist.add(enemy)

##            enemy2 = Enemy2()
##            enemy2.rect.centerx = 700
##            enemy2.rect.centery = 700
##            enemylist.add(enemy2)
            

    if rooms[0] == 0 and rooms[1] == 0:     # determin9ing the room in which the player is
            roomnumber = 1
    if rooms == [1, 0]:
            roomnumber = 4
    if rooms == [-1,-1]:
            roomnumber = 7
            #enemy = Enemy()
            enemy.rect.centerx = 100
            enemy.rect.centery = 100
            enemylist.add(enemy)
    if rooms == [0,-1]:
            roomnumber = 6
    if rooms == [1,-1]:
            roomnumber = 5

#==============================================================================
#      ________  ________  ________  _____ ______            _____             #
#     |\   __  \|\   __  \|\   __  \|\   _ \  _   \         / __  \            #
#     \ \  \|\  \ \  \|\  \ \  \|\  \ \  \\\__\ \  \       |\/_|\  \           #
#      \ \   _  _\ \  \\\  \ \  \\\  \ \  \\|__| \  \      \|/ \ \  \          #
#       \ \  \\  \\ \  \\\  \ \  \\\  \ \  \    \ \  \          \ \  \         #
#        \ \__\\ _\\ \_______\ \_______\ \__\    \ \__\          \ \__\        #
#         \|__|\|__|\|_______|\|_______|\|__|     \|__|           \|__|        #
#                                                                              #
#==============================================================================
                                       
    if roomnumber == 1:

        #===========================DEFAULT WALLS
        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 800
        walllist.add(wall)

        #=============================END

        bench = Bench(300, 300)
        bench.rect.left = 20
        bench.rect.bottom = 780
        walllist.add(bench)

        bench = Bench(300, 300)
        bench.rect.right = 780
        bench.rect.bottom = 780
        walllist.add(bench)

        #image = Image(300, 300)
        #image.rect.right = 780
        #image.rect.bottom = 780
        #imagelist.add(image)


#==============================================================================
#      ________  ________  ________  _____ ______              _____           #
#     |\   __  \|\   __  \|\   __  \|\   _ \  _   \          /  ___  \         #
#     \ \  \|\  \ \  \|\  \ \  \|\  \ \  \\\__\ \           /__/|_/  /|        #
#      \ \   _  _\ \  \\\  \ \  \\\  \ \  \\|__| \  \       |__|//  / /        #
#       \ \  \\  \\ \  \\\  \ \  \\\  \ \  \    \ \  \          /  /_/__       #
#        \ \__\\ _\\ \_______\ \_______\ \__\    \ \__\        |\________\     #
#         \|__|\|__|\|_______|\|_______|\|__|     \|__|         \|_______|     #
#                                                                              #
#==============================================================================
    if roomnumber == 2:

        #===========================DEFAULT WALLS
        wall = Wall(1100, 30, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 800
        walllist.add(wall)

        #=============================END



        wall = Wall(5, 590, WALLGREY)            #Long Wall
        wall.rect.centerx = 326
        wall.rect.bottom = 600
        walllist.add(wall)

        wall = Wall(5, 344, WALLGREY)            #Short wall
        wall.rect.centerx = 326
        wall.rect.centery = 850
        walllist.add(wall)

        wall = Wall(350, 5, WALLGREY)          #office horizontal
        wall.rect.centerx = 650
        wall.rect.centery = 477
        walllist.add(wall)

        wall = Wall(5, 320, WALLGREY)          #office verticle
        wall.rect.centerx = 477
        wall.rect.bottom = 800
        walllist.add(wall)

        wall = Wall(100, 5, DOOR)              #office door right
        wall.rect.centerx = 550
        wall.rect.centery = 477
        walllist.add(wall)

        wall = Wall(100, 5, DOOR)          #office door left
        wall.rect.centerx = 279
        wall.rect.centery = 675
        walllist.add(wall)

        wall = Wall(160, 5, WALLGREY)              #office top left (left wall)
        wall.rect.centerx = 90
        wall.rect.centery = 322.5
        walllist.add(wall)

        wall = Wall(100, 5, WALLGREY)          #office top left (right wall)
        wall.rect.right = 325
        wall.rect.centery = 322.5
        walllist.add(wall)

        wall = Wall(100, 5, WALLGREY)              #office top right (left wall)
        wall.rect.right = 800
        wall.rect.centery = 260
        walllist.add(wall)

        wall = Wall(250, 5, WALLGREY)          #office door right (right wall)
        wall.rect.left = 325
        wall.rect.centery = 260
        walllist.add(wall)


 
#==============================================================================
#      ________  ________  ________  _____ ______          ________            #
#     |\   __  \|\   __  \|\   __  \|\   _ \  _   \       |\_____  \           #
#     \ \  \|\  \ \  \|\  \ \  \|\  \ \  \\\__\ \  \      \|____|\ /_          #
#      \ \   _  _\ \  \\\  \ \  \\\  \ \  \\|__| \  \           \|\  \         #
#       \ \  \\  \\ \  \\\  \ \  \\\  \ \  \    \ \  \         __\_\  \        #
#        \ \__\\ _\\ \_______\ \_______\ \__\    \ \__\       |\_______\       #
#         \|__|\|__|\|_______|\|_______|\|__|     \|__|        \|_______|      #
#                                                                              #
#==============================================================================
    if roomnumber == 3:

        #===========================DEFAULT WALLS
        wall = Wall(1100, 30, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(30, 1100, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 800
        walllist.add(wall)

        #=============================END

#==============================================================================
#      ________  ________  ________  _____ ______         ___   ___           #
#     |\   __  \|\   __  \|\   __  \|\   _ \  _   \      |\  \ |\  \          #
#     \ \  \|\  \ \  \|\  \ \  \|\  \ \  \\\__\ \  \     \ \  \\_\  \         #
#      \ \   _  _\ \  \\\  \ \  \\\  \ \  \\|__| \  \     \ \______  \        #
#       \ \  \\  \\ \  \\\  \ \  \\\  \ \  \    \ \  \     \|_____|\  \       #
#        \ \__\\ _\\ \_______\ \_______\ \__\    \ \__\           \ \__\      #
#         \|__|\|__|\|_______|\|_______|\|__|     \|__|            \|__|      #
#                                                                             #
#==============================================================================
    if roomnumber == 4:
 
                #===========================DEFAULT WALLS
        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(30, 1100, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 800
        walllist.add(wall)

        #=============================END

#==============================================================================
#      ________  ________  ________  _____ ______            |\   ____\        #
#     |\   __  \|\   __  \|\   __  \|\   _ \  _   \          \ \  \___|_       #
#     \ \  \|\  \ \  \|\  \ \  \|\  \ \  \\\__\ \  \          \ \_____  \      #
#      \ \   _  _\ \  \\\  \ \  \\\  \ \  \\|__| \  \          \|____|\  \     #
#       \ \  \\  \\ \  \\\  \ \  \\\  \ \  \    \ \  \           ____\_\  \    #
#        \ \__\\ _\\ \_______\ \_______\ \__\    \ \__\         |\_________\   #
#         \|__|\|__|\|_______|\|_______|\|__|     \|__|         \|_________|   #
#                                                                              #
#==============================================================================
    if roomnumber == 5:

                #===========================DEFAULT WALLS
        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(1100, 30, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(30, 1100, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 800
        walllist.add(wall)

        #=============================END

#==============================================================================
#      ________  ________  ________  _____ ______             ________         #
#     |\   __  \|\   __  \|\   __  \|\   _ \  _   \          |\   ____\        #
#     \ \  \|\  \ \  \|\  \ \  \|\  \ \  \\\__\ \  \         \ \  \___|        #
#      \ \   _  _\ \  \\\  \ \  \\\  \ \  \\|__| \  \         \ \  \___        #
#       \ \  \\  \\ \  \\\  \ \  \\\  \ \  \    \ \  \         \ \  ___  \     #
#        \ \__\\ _\\ \_______\ \_______\ \__\    \ \__\         \ \_______\    #
#         \|__|\|__|\|_______|\|_______|\|__|     \|__|          \|_______|    #
#                                                                              #
#==============================================================================
    if roomnumber == 6:

                #===========================DEFAULT WALLS
        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(1100, 30, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 800
        walllist.add(wall)

        #=============================END
#==============================================================================
#      ________  ________  ________  _____ ______           ________           #
#     |\   __  \|\   __  \|\   __  \|\   _ \  _   \        |\_____  \          #
#     \ \  \|\  \ \  \|\  \ \  \|\  \ \  \\\__\ \  \        \|___/  /|         #
#      \ \   _  _\ \  \\\  \ \  \\\  \ \  \\|__| \  \           /  / /         #
#       \ \  \\  \\ \  \\\  \ \  \\\  \ \  \    \ \  \         /  / /          #
#        \ \__\\ _\\ \_______\ \_______\ \__\    \ \__\       /__/ /           #
#         \|__|\|__|\|_______|\|_______|\|__|     \|__|       |__|/            #
#                                                                              #
#==============================================================================
    if roomnumber == 7:

               #===========================DEFAULT WALLS
        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(1100, 30, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(30, 1100, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 800
        walllist.add(wall)

        #=============================END

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 800
        walllist.add(wall)

#==============================================================================
#      ________  ________  ________  _____ ______           ________           #
#     |\   __  \|\   __  \|\   __  \|\   _ \  _   \        |\   __  \          #
#     \ \  \|\  \ \  \|\  \ \  \|\  \ \  \\\__\ \  \       \ \  \|\  \         #
#      \ \   _  _\ \  \\\  \ \  \\\  \ \  \\|__| \  \       \ \   __  \        #
#       \ \  \\  \\ \  \\\  \ \  \\\  \ \  \    \ \  \       \ \  \|\  \       #
#        \ \__\\ _\\ \_______\ \_______\ \__\    \ \__\       \ \_______\      #
#         \|__|\|__|\|_______|\|_______|\|__|     \|__|        \|_______|      #
#                                                                              #
#==============================================================================
    if roomnumber == 8:

                #===========================DEFAULT WALLS
        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(30, 1100, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 800
        walllist.add(wall)

        #=============================END

        desk = FrontDesk(300, 300)
        desk.rect.centerx = 400
        desk.rect.bottom = 400
        walllist.add(desk)

        desk = FrontDesk(300, 300)
        desk.rect.centerx = 400
        desk.rect.top = 400
        walllist.add(desk)
#
        desk1 = Desk1(300, 300)
        desk1.rect.centerx = 100
        desk1.rect.bottom = 150
        walllist.add(desk1)

        desk1 = Desk1(300, 300)
        desk1.rect.centerx = 100
        desk1.rect.top = 225
        walllist.add(desk1)

        desk1 = Desk1(128, 128)
        desk1.rect.centerx = 100
        desk1.rect.top = 450
        walllist.add(desk1)

        desk1 = Desk1(128, 128)
        desk1.rect.centerx = 100
        desk1.rect.bottom = 775
        walllist.add(desk1)


#
        sofa = Sofa(300, 300)
        sofa.rect.right = 740
        sofa.rect.bottom = 780
        walllist.add(sofa)

        sofa = Sofa(128, 128)
        sofa.rect.right = 600
        sofa.rect.bottom = 780
        walllist.add(sofa)

        sofa1 = Sofa1(300, 300)
        sofa1.rect.centerx = 770
        sofa1.rect.bottom = 730
        walllist.add(sofa1)

        sofa1 = Sofa1(300, 300)
        sofa1.rect.centerx = 770
        sofa1.rect.bottom = 600
        walllist.add(sofa1)
#







#==============================================================================
#      ________  ________  ________  _____ ______           ________          #
#     |\   __  \|\   __  \|\   __  \|\   _ \  _   \        |\  ___  \         # 
#     \ \  \|\  \ \  \|\  \ \  \|\  \ \  \\\__\ \  \       \ \____   \        # 
#      \ \   _  _\ \  \\\  \ \  \\\  \ \  \\|__| \  \       \|____|\  \       #
#       \ \  \\  \\ \  \\\  \ \  \\\  \ \  \    \ \  \          __\_\  \      # 
#        \ \__\\ _\\ \_______\ \_______\ \__\    \ \__\        |\_______\     # 
#         \|__|\|__|\|_______|\|_______|\|__|     \|__|        \|_______|     #
#                                                                             #
#==============================================================================
    if roomnumber == 9:

                #===========================DEFAULT WALLS
        wall = Wall(1100, 30, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(650, 30, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(30, 1100, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 0
        wall.rect.centery = 800
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 0
        walllist.add(wall)

        wall = Wall(30, 650, LIGHTBLUE)
        wall.rect.centerx = 800
        wall.rect.centery = 800
        walllist.add(wall)

        #=============================END


        wall = Wall(100, 5, WALLGREY)                  # office horizontal
        wall.rect.right = 800
        wall.rect.centery = 200
        walllist.add(wall)

        wall = Wall(100, 5, WALLGREY)                  # office horizontal
        wall.rect.right = 650
        wall.rect.centery = 200
        walllist.add(wall)

        wall = Wall(100, 5, WALLGREY)                  # office horizontal
        wall.rect.right = 550
        wall.rect.centery = 200
        walllist.add(wall)

        wall = Wall(100, 5, WALLGREY)                  # office horizontal
        wall.rect.right = 400
        wall.rect.centery = 200
        walllist.add(wall)

        wall = Wall(100, 5, WALLGREY)                  # office horizontal
        wall.rect.right = 300
        wall.rect.centery = 200
        walllist.add(wall)

        wall = Wall(100, 5, WALLGREY)                  # office horizontal
        wall.rect.right = 150
        wall.rect.centery = 200
        walllist.add(wall)


        wall = Wall(5, 200, WALLGREY)
        wall.rect.centerx = 550
        wall.rect.top = 0
        walllist.add(wall)

        wall = Wall(5, 200, WALLGREY)
        wall.rect.centerx = 300
        wall.rect.top = 0
        walllist.add(wall)

        wall = Wall(5, 200, WALLGREY)
        wall.rect.centerx = 100
        wall.rect.top = 0
        walllist.add(wall)


#===============================================================================================
#------------------------------Variable setting/code before loop--------------------------------
#===============================================================================================

for counter in range(1):
    player = Player(100, 0, 10) #Setting Players Health and samage
    player.rect.centerx = 137 #Setting players start X co-ordinate
    player.rect.centery = 137 #Setting players start Y co-ordinate
    playerlist.add(player)



pygame.display.set_caption("Game Game") #Setting caption at top to Game

all_sprites_list.add(enemy)
all_sprites_list.add(player)

block_list.add(enemy)

#roomnumber = 1
#enemy = Enemy()
#enemy.rect.centerx = 100
#enemy.rect.centery = 100
#enemylist.add(enemy)

#enemy2 = Enemy2()
#enemy.rect.centerx = 700
#enemy.rect.centery = 700
#enemylist.add(enemy2)

ctypes.windll.user32.MessageBoxW(0, "You have 1 life, 1 mission. Find a way out", "Welcome to 9tmare", 1)
#===============================================================================================
#------------------------------------------Game Loop--------------------------------------------
#===============================================================================================
done = False

while not done:

    #Inputs

    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.centerx
            bullet.rect.y = player.rect.centery
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)

    all_sprites_list.update()



        
    if player.roomchange == 1:
        walllist = pygame.sprite.Group()
        newrooms()
        player.roomchange = 0
        print("trig")
        
    if keypress[pygame.K_LEFT]:      # if left hey is pressed
        player.velocityx = - 3       # X velocity set to go backwards
        rol = 2                      # rol value set to 2 to be used later
        for player in playerlist:    
            Player.facing(rol, uod)
    elif keypress[pygame.K_RIGHT]:   # if right key is pressed
        player.velocityx = 3        # X velocity is set to go forewards 1
        rol = 1                      # rol value set to 1
        for player in playerlist:
            Player.facing(rol, uod)

    player_x=player.rect.centerx
    player_y=player.rect.centery
         
    if keypress[pygame.K_y]:
            print("hello")
            bullet=Bullet(player_x, player_y, player.direction)
            bullet_list.add(bullet)
            bullet.move()
            
            
    
        
    if keypress[pygame.K_UP]:        # if up key is pressed 
        player.velocityy = - 3       # Y velocity set to go down 1 which is up in pygame
        uod = 1                      # uod value set to 2
        for player in playerlist:
            Player.facing(rol, uod)
    elif keypress[pygame.K_DOWN]:    # if down key is pressed
        player.velocityy = 3         # Y velocity set to go up 1 which is down in pyagme
        uod = 2                      # uod value set to 2
        for player in playerlist:
            Player.facing(rol, uod)

    if player.rect.centerx >= 50 and player.rect.centerx <= 100 and player.rect.centery >= 50 and player.rect.centery <= 100 and rooms == [-1, 1] and keypress[pygame.K_f]:
        ctypes.windll.user32.MessageBoxW(0, "You found a key, but whats it for?", "Alert", 1)
        key = 1

    if key == 1 and player.rect.centerx >= 700 and player.rect.centerx <= 800 and player.rect.centery >= 0 and player.rect.centery <= 100 and rooms == [1, -1] and keypress[pygame.K_f]:
        ctypes.windll.user32.MessageBoxW(0, "you made it out!!", "Congratulations", 1)
        break


         
    for player in playerlist:
         Player.moving()
         Player.newroomchange()



    # Searching zone, multiple of the smae systems


    #end of searching zones



    for enemy in enemylist:
         Enemy.move(1)

    for enemy2 in enemylist:
        Enemy2.move(1)

    for bullet in bullet_list:
        bullet.move()

    if player.roomchange == 1:
            enemylist.remove(enemy)

    if player.roomchange == 1:
            enemylist.remove(enemy2)

##    if pygame.spritecollide(bullet_list, enemylist):
##            enemylist.remove(enemy)
##            bullet_list.remove(bullet)
    bullet_hit_list = pygame.sprite.spritecollide(enemy, bullet_list, True)

    for bullet in bullet_hit_list:
        enemylist.remove(enemy)
        all_sprites_list.remove(bullet)
        score += 1
        

    for wall in walllist:                                                                                 #========================================================================================
        if player.rect.left >= wall.rect.left and player.rect.right <= wall.rect.right:                   # THE FOLLOWING IS CHECKING WHETHER OR NOT THE PLAYER OR ENEMYIES LOCATION IS EQUAL TO ONE OF THE WALLS
            if player.rect.bottom >= wall.rect.top and player.rect.top <= wall.rect.top:                  # IN WHICH CASE, VELOCITY IS SET TO 0 AND THE PLAYER OR ENEMY IS UNABLE TO MOVE 

                if uod == 2:
                    player.rect.bottom = wall.rect.top
                
                
            if player.rect.top <= wall.rect.bottom and player.rect.bottom >= wall.rect.bottom:

                if uod == 1:
                    player.rect.top = wall.rect.bottom

        elif player.rect.left <= wall.rect.right and player.rect.left >= wall.rect.left:
            if player.rect.bottom >= wall.rect.top and player.rect.top <= wall.rect.top:

                if rol == 2:
                    player.rect.left = wall.rect.right
                elif rol == 1:
                    rol = 1

                elif uod == 2:
                     player.rect.bottom = wall.rect.top
                
            if player.rect.top <= wall.rect.bottom and player.rect.bottom >= wall.rect.bottom:
                
                if rol == 2:
                    player.rect.left = wall.rect.right
                    
            if player.rect.top >= wall.rect.top and player.rect.bottom <=wall.rect.bottom:

                if rol == 2:
                    player.rect.left = wall.rect.right
                              
            
        elif player.rect.right >= wall.rect.left and player.rect.right <= wall.rect.right:
            if player.rect.bottom >= wall.rect.top and player.rect.top <= wall.rect.top:

                if rol == 1:
                    player.rect.right = wall.rect.left
                
                
            if player.rect.top <= wall.rect.bottom and player.rect.bottom >= wall.rect.bottom:

                if rol == 1:
                    player.rect.right = wall.rect.left
                
                
            if player.rect.top >= wall.rect.top and player.rect.bottom <=wall.rect.bottom:

                if rol == 1:
                    player.rect.right = wall.rect.left

#==========================================================

        if enemy.rect.left >= wall.rect.left and enemy.rect.right <= wall.rect.right:
            if enemy.rect.bottom >= wall.rect.top and enemy.rect.top <= wall.rect.top:

                
                enemy.rect.bottom = wall.rect.top
                
                
            if enemy.rect.top <= wall.rect.bottom and enemy.rect.bottom >= wall.rect.bottom:

                
                enemy.rect.top = wall.rect.bottom

        elif enemy.rect.left <= wall.rect.right and enemy.rect.left >= wall.rect.left:
            if enemy.rect.bottom >= wall.rect.top and enemy.rect.top <= wall.rect.top:

                
                enemy.rect.left = wall.rect.right
                

               
                enemy.rect.bottom = wall.rect.top
                
            if enemy.rect.top <= wall.rect.bottom and enemy.rect.bottom >= wall.rect.bottom:
                
                
                enemy.rect.left = wall.rect.right
                    
            if enemy.rect.top >= wall.rect.top and enemy.rect.bottom <=wall.rect.bottom:

                
                enemy.rect.left = wall.rect.right
                              
            
        elif enemy.rect.right >= wall.rect.left and enemy.rect.right <= wall.rect.right:
            if enemy.rect.bottom >= wall.rect.top and enemy.rect.top <= wall.rect.top:

                
                enemy.rect.right = wall.rect.left
                
                
            if enemy.rect.top <= wall.rect.bottom and enemy.rect.bottom >= wall.rect.bottom:

                
                enemy.rect.right = wall.rect.left
                
                
            if enemy.rect.top >= wall.rect.top and enemy.rect.bottom <=wall.rect.bottom:

                
                enemy.rect.right = wall.rect.left


#Enemy 2


        if enemy2.rect.left >= wall.rect.left and enemy2.rect.right <= wall.rect.right:
            if enemy2.rect.bottom >= wall.rect.top and enemy2.rect.top <= wall.rect.top:

                
                enemy2.rect.bottom = wall.rect.top
                
                
            if enemy2.rect.top <= wall.rect.bottom and enemy2.rect.bottom >= wall.rect.bottom:

                
                enemy2.rect.top = wall.rect.bottom

        elif enemy2.rect.left <= wall.rect.right and enemy2.rect.left >= wall.rect.left:
            if enemy2.rect.bottom >= wall.rect.top and enemy2.rect.top <= wall.rect.top:

                
                enemy2.rect.left = wall.rect.right
                

               
                enemy.rect.bottom = wall.rect.top
                
            if enemy2.rect.top <= wall.rect.bottom and enemy2.rect.bottom >= wall.rect.bottom:
                
                
                enemy2.rect.left = wall.rect.right
                    
            if enemy2.rect.top >= wall.rect.top and enemy2.rect.bottom <=wall.rect.bottom:

                
                enemy2.rect.left = wall.rect.right
                              
            
        elif enemy2.rect.right >= wall.rect.left and enemy2.rect.right <= wall.rect.right:
            if enemy2.rect.bottom >= wall.rect.top and enemy2.rect.top <= wall.rect.top:

                
                enemy2.rect.right = wall.rect.left
                
                
            if enemy2.rect.top <= wall.rect.bottom and enemy2.rect.bottom >= wall.rect.bottom:

                
                enemy2.rect.right = wall.rect.left
                
                
            if enemy2.rect.top >= wall.rect.top and enemy2.rect.bottom <=wall.rect.bottom:

                
                enemy2.rect.right = wall.rect.left



                                                                                                                         #END


        if enemy.rect.centerx == player.rect.centerx and enemy.rect.centery == player.rect.centery or enemy2.rect.centerx == player.rect.centerx and enemy2.rect.centery == player.rect.centery:

                player.roomchange = 1                   #is the player and the enemy is the same position, if so increase deaths, set postion back to origional and start screen
                rooms = [0,0]
                player.rect.centerx = 137 
                player.rect.centery = 137
                deaths = deaths + 1
                key = 0
                enemylist.remove(enemy)
                enemylist.remove(enemy)
                score = 0

        if enemy2.rect.centerx == player.rect.centerx and enemy2.rect.centery == player.rect.centery:

                player.roomchange = 1                   #is the player and the enemy is the same position, if so increase deaths, set postion back to origional and start screen
                rooms = [0,0]
                player.rect.centerx = 137 
                player.rect.centery = 137
                deaths = deaths + 1
                key = 0
                enemylist.remove(enemy)
                enemylist.remove(enemy2)
                score = 0
                scoretext = myfont.render("Score {0}".format(score), 1, (255,0,0))
                screen.blit(scoretext, (625, 10))
        if deaths == 100:
                ctypes.windll.user32.MessageBoxW(0, "Game Over", "Alert", 1)
                testVar = input("Save Highscore. Name?")
                with open('scores.txt', 'w') as output:
                        output.write("HIGHSCORE: " )
                        output.write(testVar)
                        output.write(":")
                        output.write(" ")
                        output.write(str(score))
                pygame.quit()

    keypress = pygame.key.get_pressed()        

    screen.fill(BROWN)               # Screen fill BROWN


    bullet_list.draw(screen)
    imagelist.draw(screen)
    enemylist.draw(screen)    
    walllist.draw(screen)    
    playerlist.draw(screen)         # draw the player onto pf the screen
    player.velocityx = 0            # default x velocity = 0
    player.velocityy = 0            # default y velocity = 0

    deathstext = myfont.render("Deaths {0}".format(deaths), 1, (0,0,0))
    screen.blit(deathstext, (5, 10))

    scoretext = myfont.render("Score {0}".format(score), 1, (0,0,0))
    screen.blit(scoretext, (625, 10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

