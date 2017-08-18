import pygame

pygame.init()

RED = (255,0,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen= pygame.display.set_mode((640,480))

clock = pygame.time.Clock()

pygame.display.set_caption("Name")

done = False

while not done:

    #Inputs

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True

    screen.fill(COLOUR)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

