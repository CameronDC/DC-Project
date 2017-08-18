import pygame

pygame.init()

RED = (255,0,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = ( 128, 128, 128)

playerlist = pygame.sprite.Group()
screen= pygame.display.set_mode((640,480))#Screen size
keypress = pygame.key.get_pressed() 
rol = 0
uod = 0
clock = pygame.time.Clock()

##Classes##
class Player(pygame.sprite.Sprite):
        def __init__(self, health, zero, damage):
            self.health = health
            self.velocityx = zero
            self.velocityy = zero
            self.damage = damage
            super().__init__()
            self.image = pygame.image.load("N.png")
            self.rect = self.image.get_rect()

        def facing(rol, uod):
            if keypress[pygame.K_RIGHT]:
                if keypress[pygame.K_UP]:
                    player.image = pygame.image.load("NE.png")
                elif keypress[pygame.K_DOWN]:
                    player.image = pygame.image.load("SE.png")
                else:
                    player.image = pygame.image.load("E.png")
            elif keypress[pygame.K_LEFT]:
                if keypress[pygame.K_UP]:
                    player.image = pygame.image.load("NW.png")
                elif keypress[pygame.K_DOWN]:
                    player.image = pygame.image.load("SW.png")
                else:
                    player.image = pygame.image.load("W.png")
            elif keypress[pygame.K_DOWN]:
                player.image = pygame.image.load("S.png")
            else:
                player.image = pygame.image.load("N.png")
                
        def moving():
            player.rect.centerx = player.rect.centerx + player.velocityx
            player.rect.centery = player.rect.centery + player.velocityy

for counter in range(1):
    player = Player(100, 0, 10)
    player.rect.centerx = 137
    player.rect.centery = 137
    playerlist.add(player)

pygame.display.set_caption("Game")

done = False

while not done:

    #Inputs

    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True

    
        
    if keypress[pygame.K_LEFT]:
        player.velocityx = - 1
        rol = 2
        for player in playerlist:
            Player.facing(rol, uod)
    elif keypress[pygame.K_RIGHT]:
        player.velocityx = 1
        rol = 1
        for player in playerlist:
            Player.facing(rol, uod)
    
        
    if keypress[pygame.K_UP]:
        player.velocityy = - 1
        uod = 1
        for player in playerlist:
            Player.facing(rol, uod)
    elif keypress[pygame.K_DOWN]:
        player.velocityy = 1
        uod = 2
        for player in playerlist:
            Player.facing(rol, uod)
    
        
    for player in playerlist:
         Player.moving()

    

        
    keypress = pygame.key.get_pressed()        
   
    screen.fill(GRAY)
    playerlist.draw(screen)
    player.velocityx = 0
    player.velocityy = 0
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

