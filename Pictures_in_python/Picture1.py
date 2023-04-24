import pygame
from pygame.draw import *
pygame.init()
screen = pygame.display.set_mode((600, 400))

screen.fill((255,255,255))

circle(screen, (255, 255, 55), (300,200),150)
circle(screen, (0, 0, 0), (300,200),151,2)
circle(screen, (255, 0, 0), (230,160),30)
circle(screen, (255, 0, 0), (370,160),20)
circle(screen, (0, 0, 0), (230,160),31,2)
circle(screen, (0, 0, 0), (370,160),21,2)
circle(screen, (0, 0, 0), (230,160),10)
circle(screen, (0, 0, 0), (370,160),7)
#rect(screen,(0, 0, 0), (20,20),(10, 10, 20, 20))

'''circle(screen, (255, 255, 55), (300,200),150)
circle(screen, (0, 0, 0), (300,200),152,2)
circle(screen, (255, 255, 55), (300,200),150)
circle(screen, (0, 0, 0), (300,200),152,2)'''

clock = pygame.time.Clock()


pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        
