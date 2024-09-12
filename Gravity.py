# import pygame
# pygame.init()
from math import sin as s
from math import cos as c
from math import atan2 as t

import pygame
import math as m
from random import randint as ri
pygame.init()

try:
    space = pygame.display.set_mode((500,500))
    pygame.display.set_caption('Solar System')
    run = True
    ps = []    
    star = {'m':500,'x':200,'y':250,'xv':0,'yv':-5}
    planet = {'m':500,'x':300,'y':250,'xv':0,'yv':5}
    ps.append(star)
    ps.append(planet)

    while run:
        pygame.display.update()
        space.fill((0,0,0))
        pygame.time.delay(50)
        
        for a,pa in enumerate(ps):
            pygame.draw.circle(space,(255,255,255),(int(pa['x']),int(pa['y'])),int(pa['m']**(1/3)))
            for b,pb in enumerate(ps):
                if a!=b:
                    dr= t(pa['y']-pb['y'],    pa['x']-pb['x'])
                    mg= (pa['y']-pb['y'])**2+(pa['x']-pb['x'])**2+1000*pa['m']**(1/3)
                    ps[a]['xv']-=c(dr)*pa['m']*pb['m']/mg/10
                    ps[a]['yv']-=s(dr)*pa['m']*pb['m']/mg/10
        for a,pa in enumerate(ps):
            ps[a]['x']+=pa['xv']
            ps[a]['y']+=pa['yv']

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                
finally:
    pygame.quit()


'''
try:
    running=True
    space = pygame.display.set_mode((500,500))
    pygame.display.set_caption('Solar System')
    
    ps = []    
    star = {'m':1000,'x':250,'y':250,'xv':0,'yv':0}
    planet = {'m':50,'x':400,'y':250,'xv':0,'yv':25}
    ps.append(star)
    ps.append(planet)
    k=0
    while k<1000:
        k+=1
        pygame.display.update()
        space.fill((0,0,0))
        pygame.time.delay(50)
        
        for a,pa in enumerate(ps):
            pygame.draw.circle(space,(255,255,255),(int(pa['x']),int(pa['y'])),int(pa['m']**(1/3)))
            for b,pb in enumerate(ps):
                if a!=b:
                    dr= t(pa['y']-pb['y'],    pa['x']-pb['x'])
                    mg= (pa['y']-pb['y'])**2+(pa['x']-pb['x'])**2
                    ps[a]['xv']+=c(dr)*pa['m']*pb['m']/mg
                    ps[a]['yv']+=s(dr)*pa['m']*pb['m']/mg
            ps[a]['x']+=pa['xv']
            ps[a]['y']+=pa['yv']
            
    
    
finally:
    pygame.quit()
'''