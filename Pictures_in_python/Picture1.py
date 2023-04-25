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
polygon(screen,(0, 0, 0),((170,90),(140,60),(280,140),(279, 145)))
polygon(screen,(0, 0, 0),((450,90),(470,70),(327,145),(330, 145)))
rect(screen,(0, 0, 0),(225,275,150, 31))
rect(screen,(255,255,255),(270,275,20, 15))
rect(screen,(255,255,255),(320,275,20, 18))
rect(screen,(255,255,255),(295,290,20, 18))

clock = pygame.time.Clock()


pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        
