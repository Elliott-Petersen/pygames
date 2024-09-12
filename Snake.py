import pygame
from random import randint as ri
pygame.init()

def snake(Size=6,time=400):
    if Size<2:
        Size=2
    try:
        window = pygame.display.set_mode((420,420))
        pygame.display.set_caption('snake')
        
        x=y=0
        w=h=xv=yv=420/Size
        run = True
        b=''
        s=[(x,y,w,h)]
        l=1
        a=(x,y,w,h)
        while run:
            pygame.time.delay(time)
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run=False
                elif event.type == pygame.KEYDOWN:
                    b=event.dict['key']
            if b==119 or b==273: #up
                y-=yv
            if b==115 or b==274: #down
                y+=yv
            if b==100 or b==275: #right
                x+=xv
            if b== 97 or b==276: #left
                x-=xv
                
            window.fill((0,0,0))
            if (x,y,w,h) in s and (x,y,w,h)!=s[0]:
                print('you crashed into yourself! :(')
                run=False
            if not (0<=x<420 and 0<=y<420):
                print('you hit the wall :(')
                run=False
            s.append((x,y,w,h))
            if len(s)>l:
                del s[0]
            for i in range(len(s)):
                pygame.draw.rect(window,(0,255*i/l,255-255*i/l),s[i])
            if s[-1]==a:
                l+=1
                if l==2*Size**2//2:
                    print('you won! :)')
                    run=False
                    pygame.display.update()
                    break
            while a in s:
                a=(ri(0,Size-1)*w,ri(0,Size-1)*w,w,h)
            
            pygame.draw.rect(window,(255,0,0),a)
            pygame.display.update()
    
    finally:
        pygame.quit()

snake(10,200)


