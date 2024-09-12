import pygame
import math as m
from random import randint as ri
pygame.init()

try:
    window = pygame.display.set_mode((500,500))
    pygame.display.set_caption('Asteroids')
    blts=[]
    rks=[]
    x=y=250
    w=50
    h=50
    fv=tv=xv=yv=0
    td=-m.pi/2
    run = True
    c=0
    t=0
    inv=0
    h=3
    while run:
        pygame.display.update()
        window.fill((0,0,0))
        pygame.time.delay(50)
        fa=ta=0
        c+=1
        t+=1
        inv+=1
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                
        keys = pygame.key.get_pressed()
        # try:
        #     print(keys.index(1))
        # except:
        #     pass
        if keys[119]==1 or keys[273]==1: #up
            fa=1
        if keys[115]==1 or keys[274]==1: #down
            fa=-1
        if keys[100]==1 or keys[275]==1: #right
            ta=0.01*m.pi
        if keys[97] ==1 or keys[276]==1: #left
            ta=-0.01*m.pi
        tv+=ta
        td+=tv
        xv+=fa*m.cos(td)
        yv+=fa*m.sin(td)
        x+=xv
        y+=yv
        
        p0 = (x+25*m.cos(td),
              y+25*m.sin(td))
        p1 = (x+25*m.cos(td+m.pi*5/6),
              y+25*m.sin(td+m.pi*5/6))
        p2 = (x+25*m.cos(td-m.pi*5/6),
              y+25*m.sin(td-m.pi*5/6))
        p=p0,p1,p2
        
        if x<0:
            x+=500
        elif x>500:
            x-=500
        if y<0:
            y+=500
        elif y>500:
            y-=500
            
        if t>=30:
            t=0
            side=ri(1,4)
            place=ri(-50,550)
            angle=ri(125,875)*m.pi/1000
            angle+=side*m.pi/2
            if side==1:
                rx,ry = 550,place
            elif side==4:
                rx,ry = place,-50
            elif side==3:
                rx,ry = -50,place
            elif side==2:
                rx,ry = place,550
            rxv,ryv=5*m.cos(angle),5*m.sin(angle)
            rks.append([rx,ry,rxv,ryv,25,angle])
        
        # rks = [rk for rk in rks if (-51<rk[0]<551 and -51<rk[1]<551)]
        for i in range(len(rks)):    
            rks[i][0]+=rks[i][2]
            rks[i][1]+=rks[i][3]
            pygame.draw.circle(window,(255,255,255),(int(rks[i][0]),int(rks[i][1])),rks[i][4])

        blts = [blt for blt in blts if (0<blt[0]<500 and 0<blt[1]<500)]                
        
        if (keys[32]==1 or keys[60]==1) and c>=10:
            c=0
            blts.append(list(p0)+[xv+15*m.cos(td)+30*tv*m.cos(td+m.pi/2),yv+15*m.sin(td)+30*tv*m.sin(td+m.pi/2)])
        for i in range(len(blts)):    
            blts[i][0]+=blts[i][2]
            blts[i][1]+=blts[i][3]
            pygame.draw.circle(window,(255,255,255),(int(blts[i][0]),int(blts[i][1])),3)
        
        for i,rk in enumerate(rks):
            for po in p:
                if (po[0]-rk[0])**2+(po[1]-rk[1])**2<625:
                    if inv>=20:
                        inv=0
                        h-=1
                        c=0
            for j,blt in enumerate(blts):
                if (blt[0]-rk[0])**2+(blt[1]-rk[1])**2<625:
                    if rk[4]==25:
                        rks.append([rk[0],rk[1],7.5*m.cos(rk[5]+m.pi/4),7.5*m.sin(rk[5]+m.pi/4),12,rk[5]+m.pi/4])
                        rks.append([rk[0],rk[1],7.5*m.cos(rk[5]-m.pi/4),7.5*m.sin(rk[5]-m.pi/4),12,rk[5]-m.pi/4])
                        
                    del rks[i]
                    del blts[j]
                    
                    break
            else:
                continue
            break
            
        if inv>20 or inv%4>1:
            pygame.draw.polygon(window,(255,255,255),p)
        if h==0:
            print('Your hull was breached :(')
            run=False
finally:
    pygame.quit()
