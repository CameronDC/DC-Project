import pygame
import os

pygame.init()

RED = (255,0,0)               #Definign Colours
GREEN = (0, 255, 0)           #       v
BLUE = (0, 0, 255)            #       v
GRAY = ( 128, 128, 128)       #----------------

walls = []
playerlist = pygame.sprite.Group() #putting player in its own list
screen= pygame.display.set_mode((400, 400))#Screen size
keypress = pygame.key.get_pressed() 
rol = 0 #right or left setting to 0
uod = 0 # setting up or down to 0
clock = pygame.time.Clock() #taking the pygame clock

#==============================================================================================
#--------------------------------------------Classes-------------------------------------------
#==============================================================================================

class Player(pygame.sprite.Sprite):
        def __init__(self, health, zero, damage):
            self.health = health        #Creating attributes of PLAYER to be used later in game
            self.velocityx = zero       #                         v
            self.velocityy = zero       #                         v
            self.damage = damage        #------------------------------------------------------
            super().__init__()
            self.image = pygame.image.load("N.png") #Load default image for player
            self.rect = self.image.get_rect()

        def facing(rol, uod):
            if keypress[pygame.K_RIGHT]: #Determining the durection of user (If Right AND....
                if keypress[pygame.K_UP]: #If Right and up 
                    player.image = pygame.image.load("NE.png") #Change player image to NE.png
                elif keypress[pygame.K_DOWN]: #If right and down
                    player.image = pygame.image.load("SE.png") #Change player image to SE.png
                else: #If it isnt up or down or left then it must be right which is East
                    player.image = pygame.image.load("E.png") #change player image to E.png
            elif keypress[pygame.K_LEFT]: #Same system with the left side of the compass
                if keypress[pygame.K_UP]: #If left and up
                    player.image = pygame.image.load("NW.png") #Change player image to NW.png
                elif keypress[pygame.K_DOWN]: #If left and down
                    player.image = pygame.image.load("SW.png") #Change player image to SW.png
                else: #If it isnt up or down or right then it must be left which is West
                    player.image = pygame.image.load("W.png") #Change player image to W.png
            elif keypress[pygame.K_DOWN]:                  #Is it north or south and changing
                player.image = pygame.image.load("S.png")  #              Image
            else:                                          #                v
                player.image = pygame.image.load("N.png")  #---------------------------------
                
        def moving(): #Moving function consisting of direction + the determined velocity.
            player.rect.centerx = player.rect.centerx + player.velocityx
            player.rect.centery = player.rect.centery + player.velocityy

        
class Wall(pygame.sprite.Sprite):
    
    def __init__(self, pos):
        walls.append(self)
        self.image = pygame.image.load("walls.jpg")
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
    

#===============================================================================================
#------------------------------Variable setting/code before loop--------------------------------
#===============================================================================================

for counter in range(1):
    player = Player(100, 0, 10) #Setting Players Health and samage
    player.rect.centerx = 137 #Setting players start X co-ordinate
    player.rect.centery = 137 #Setting players start Y co-ordinate
    playerlist.add(player)

pygame.display.set_caption("Game Game") #Setting caption at top to Game

level = [
"WWWWWWWWWW     WWWWWWWWWWWWWWW",
"W                       W",
"W                       W",
"W                       W",
"W                       W",
"W                       W",
"W                       W",
"W                       W",
"W                       W",
"                       ",
"                      ",
"                       ",
"                       ",
"W                       W",
"W                       W",
"W                       W",
"W                       W",
"W                       W",
"W                       W",
"W                       W",
"W                       W",
"W                       W",
"W                       W",
"W                       W",
"WWWWWWWWWW     WWWWWWWWWWWWWWW",
]

x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0


#===============================================================================================
#------------------------------------------Game Loop--------------------------------------------
#===============================================================================================
done = False

while not done:

    #Inputs

    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True

    
        
    if keypress[pygame.K_LEFT]:      # if left hey is pressed
        player.velocityx = - 1       # X velocity set to go backwards
        rol = 2                      # rol value set to 2 to be used later
        for player in playerlist:    
            Player.facing(rol, uod)
    elif keypress[pygame.K_RIGHT]:   # if right key is pressed
        player.velocityx = 1         # X velocity is set to go forewards 1
        rol = 1                      # rol value set to 1
        for player in playerlist:
            Player.facing(rol, uod)
    
        
    if keypress[pygame.K_UP]:        # if up key is pressed 
        player.velocityy = - 1       # Y velocity set to go down 1 which is up in pygame
        uod = 1                      # uod value set to 2
        for player in playerlist:
            Player.facing(rol, uod)
    elif keypress[pygame.K_DOWN]:    # if down key is pressed
        player.velocityy = 1         # Y velocity set to go up 1 which is down in pyagme
        uod = 2                      # uod value set to 2
        for player in playerlist:
            Player.facing(rol, uod)
    
        
    for player in playerlist:
         Player.moving()

        
    keypress = pygame.key.get_pressed()        

    screen.fill(GRAY)               # Screen fill GRAY
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
        
        
    playerlist.draw(screen)         # draw the player onto pf the screen
    player.velocityx = 0            # default x velocity = 0
    player.velocityy = 0            # default y velocity = 0
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

