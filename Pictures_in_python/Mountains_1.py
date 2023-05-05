import pygame
from pygame.draw import *
pygame.init()
#Set the display size
screen  = pygame.display.set_mode((1000, 700))

screen.fill((186,130,147))
def background():
    '''Set the display background. It is three parallel rectangles different colors
    representing tones of the sunset sky and the lower darker part is a background.'''
    rect(screen,(255,214,153),(0,0,1000, 170))
    rect(screen,(255,212,192),(0,170,1000, 150))
    rect(screen,(255,214,137),(0,320,1000, 150))
def sun():
    '''Creates a sun with a circle shape'''
    circle(screen,(251,245,0),(500,170),70)
def mountains():
    '''Creates a mountains with different shapes'''
    def mountain1():
        '''Creates a mountain that shape are tilted to the horizon'''
        mountain_1_peakescoordinates = [(0,340),(10,300),(200,152),(240, 160),(260,200),
                                        (370,250),(410,230),(450,285),(510,270),(570,230),
                                        (600,250),(640,230),(720,140),(735,144),(790,200),
                                        (850,180),(900,215),(1000,230)]
        for i in range(10,210,10):  #This cycle addes smooth shape to one of the peakes in mountain_1_peakescoordinates
            n = 343+10500/(i-255)
            mountain_1_peakescoordinates.insert(int(1+i/10),(i,n))
        polygon(screen,(255, 149, 0),mountain_1_peakescoordinates)
        ellipse(screen,(255, 149, 0),(690,140,70, 120)) #This shape addes smoothness to one of the peakes

    def mountain2():
        '''Creates a mountain that shape are parallel to the horizon'''
        mountain_2_peakescoordinates = ((0,500),(0,350),(20,370),(75, 330),(90,305),
                                        (190,470),(220,400),(290,440),(370,320),(420,340,),
                                        (480,420),(560,395),(640,330),(720,305),(800,400),
                                        (850,330),(900,380),(940,320),(1000,260),(1000,500))
        polygon(screen,(184, 56, 36),mountain_2_peakescoordinates)
        ellipse(screen,(184, 56, 36),(15,300,110, 190)) #This shape addes smoothness to one of the peakes
        

    def mountain3():
        '''Creates a mountain in a front row'''
        mountain_3_peakescoordinates = ((0,700),(0,300),(100,350),(200,550),(300,650),
                                        (500,670),(700,550),(750,600),(800,630),(900,450),
                                        (1000,430),(1000,700))
        polygon(screen,(52, 10, 38),mountain_3_peakescoordinates)
    mountain1()
    mountain2()
    mountain3()
def birds():
    '''Creates a birds in a simple V shape'''
    polygon(screen,(70, 31, 2),((200,200),(220,210),(240,200),(220,220),(200,200)))
    polygon(screen,(70, 31, 2),((100,100),(120,110),(140,100),(120,120),(100,100)))
    polygon(screen,(70, 31, 2),((300,300),(320,310),(340,300),(320,320),(300,300)))
    polygon(screen,(70, 31, 2),((150,150),(170,160),(190,150),(170,170),(150,150)))
    
background()
sun()
mountains()
birds()





clock = pygame.time.Clock()


pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
