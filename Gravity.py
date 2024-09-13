import pygame
from math import sin as s
from math import cos as c
from math import atan2 as t

pygame.init()
try:
    space = pygame.display.set_mode((500,500))
    pygame.display.set_caption('Solar System')
    run = True
    ps = []    
    star = {'m':500,'x':100,'y':250,'xv':0,'yv':-.5}
    planet = {'m':500,'x':400,'y':250,'xv':0,'yv':.5}
    ps.append(star)
    ps.append(planet)

    while run:
        pygame.display.update()
        space.fill((0,0,0))
        pygame.time.delay(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                p = list(event.dict['pos'])
            elif event.type == pygame.MOUSEBUTTONUP:
                q = list(event.dict['pos'])
                ps.append({'m':500,'x':p[0],'y':p[1],'xv':(q[0]-p[0])/50,'yv':(q[1]-p[1])/50})
            
        for a,pa in enumerate(ps):
            pygame.draw.circle(space,(255,255,255),(int(pa['x']),int(pa['y'])),int(pa['m']**(1/3)))
            for b,pb in enumerate(ps):
                if (pa['y'],pa['x'])!=(pb['y'],pb['x']):
                    dr= t(pa['y']-pb['y'],    pa['x']-pb['x'])
                    di= max(((pa['y']-pb['y'])**2+(pa['x']-pb['x'])**2)**.5,50)
                    ps[a]['xv']-=(c(dr)*pb['m']/di**2)
                    ps[a]['yv']-=(s(dr)*pb['m']/di**2)
        for a,pa in enumerate(ps):
            ps[a]['x']+=pa['xv']
            ps[a]['y']+=pa['yv']
                
finally:
    pygame.quit()

