import pygame
import random

pygame.init()

BLACK =[0,0,0]
WHITE = [255,255,255,]
SIZE = [400,400]

bg = pygame.image.load('xmasni8.jpg')

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Sow Night")

snow_list =[]

for i in range(70):
    x= random.randrange(0,400)
    y= random.randrange(0,400)
    snow_list.append([x,y])
clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             done = True
           
    screen.fill(BLACK)
    screen.blit(bg,(0,0))

    for i in range(len(snow_list)):
        pygame.draw.circle(screen, WHITE, snow_list[i], 4)
        snow_list[i][1] += 1

        if snow_list[i][1] > 400:
            y = random.randrange(-50,-10)
            snow_list[i][1] =y
            x = random.randrange(0,400)
            snow_list[i][0] =x

    pygame.display.flip()
    clock.tick(150)
pygame.quit()



