import pygame, random, sys
pygame.init()

#draw window
screen=pygame.display.set_mode((673,673))
pygame.display.set_caption('Invasion')
clock=pygame.time.Clock()

font1=pygame.font.SysFont('arial',24)

def fill():
    screen.fill((190,253,144)) #140,203,94
def grid():
    for x in range(33):
        pygame.draw.line(screen,(0,0,0),[x*21,0],[x*21,673])
        pygame.draw.line(screen,(0,0,0),[0,x*21],[673,x*21])
def drawpixel(x,y,color):
    pygame.draw.rect(screen,color,([x*21+1,y*21+1],[20,20]))
def drawrect(x,y,a,b,color):
    pygame.draw.rect(screen,color,([x*21+1,y*21+1],[a*21,b*21]))
def sq(i,o):
    s=set()
    for x in range(i[0]):
        for y in range(i[1]):
            s.add((x+o[0],y+o[1]))
    return s
def fig_move():
    global fig_pos, first_move
    fig_pos[0]+=xchanger
    fig_pos[1]+=ychanger
    if fig_pos[1]<0:
        fig_pos[1]=0
    if fig_pos[1]+fig_size[1]>31:
        fig_pos[1]=32-fig_size[1]
    if fig_pos[0]+fig_size[0]>31:
        fig_pos[0]=32-fig_size[0]
    if fig_pos[0]<0:
        fig_pos[0]=0
    first_move=False
def check_move():
    ret=True
    for i in territory:
        if sq(fig_size,fig_pos)&i:
            ret=False
    if ret:
        ret=False
        a=[fig_pos[0]+1,fig_pos[1]]
        if sq(fig_size,a)&territory[who_pl]:
            ret=True
        if not ret:
            a=[fig_pos[0]-1,fig_pos[1]]
            if sq(fig_size,a)&territory[who_pl]:
                ret=True
        if not ret:
            a=[fig_pos[0],fig_pos[1]+1]
            if sq(fig_size,a)&territory[who_pl]:
                ret=True
        if not ret:
            a=[fig_pos[0],fig_pos[1]-1]
            if sq(fig_size,a)&territory[who_pl]:
                ret=True
    return ret
def start_screen():
    fill()
    label="ASDW or arrows - move"
    text=font1.render(label,1,(0,0,0))
    screen.blit(text,(50,50))
    label="Shift - spin"
    text=font1.render(label,1,(0,0,0))
    screen.blit(text,(60,75))
    label="SPACE - finish the move"
    text=font1.render(label,1,(0,0,0))
    screen.blit(text,(70,100))
    label="F - skip the move"
    text=font1.render(label,1,(0,0,0))
    screen.blit(text,(80,125))
    label="Players: "+str(players)
    text=font1.render(label,1,(0,0,0))
    screen.blit(text,(90,150))
    label="Press Space"
    text=font1.render(label,1,(0,0,0))
    screen.blit(text,(100,175))
    grid()
def gameover_screen():
    fill()
    grid()
    sc=[]
    nm=[]
    while score!=[] or names!=[]:
        a=score.index(max(score))
        sc.append(score[a])
        nm.append(names[a])
        score.remove(score[a])
        names.remove(names[a])
    label="Game Over"
    text=font1.render(label,1,(0,0,0))
    screen.blit(text,(50,50))
    label="    Winner: {}, {}".format(nm[0],sc[0])
    text=font1.render(label,1,(0,0,0))
    screen.blit(text,(50,75))
    label="    2: {}, {}".format(nm[1],sc[1])
    text=font1.render(label,1,(0,0,0))
    screen.blit(text,(50,100))
    if players==4:
        label="    3: {}, {}".format(nm[2],sc[2])
        text=font1.render(label,1,(0,0,0))
        screen.blit(text,(50,125))
        label="    4: {}, {}".format(nm[3],sc[3])
        text=font1.render(label,1,(0,0,0))
        screen.blit(text,(50,150))
    pygame.display.update()
try:
    interrupt=False
    while not interrupt:
        players=2
        start_screen()
        bug=True
        while bug and not interrupt:
            for x in pygame.event.get(): #keyboard
                if x.type == pygame.QUIT:
                    interrupt=True
                if x.type==pygame.KEYDOWN:
                    if x.key==pygame.K_d or x.key==pygame.K_RIGHT or x.key==pygame.K_a or x.key==pygame.K_LEFT:
                        if players==2:
                            players=4
                        else:
                            players=2
                        start_screen()
                    if x.key==pygame.K_SPACE:
                        bug=False
                pygame.display.update()
            clock.tick(30)

        names=["Red","Blue","Yellow","Grey"]
        score=[0,0,0,0]
        corner=[[0,0],[31,31],[31,0],[0,31]]
        territory=[{(-1,0),(0,-1)},{(31,32),(32,31)},{(31,-1),(32,0)},{(-1,31),(0,32)}]
        colors=[(255,100,100),(100,100,255),(255,255,0),(100,100,100)]
        colors2=[(255,150,150),(150,150,255),(255,255,125),(150,150,150)]
        who_pl=0
        pygame.display.update()
        skip_counter=0
        while skip_counter<4 and not interrupt:
            #current var
            xchanger=0
            ychanger=0
            pl_color=colors[who_pl]
            pl_color2=colors2[who_pl]
            fig_pos=[13,13]
            fig_size=[random.randint(1,4),random.randint(1,4)] #6
            fig_square=fig_size[0]*fig_size[1]
            move=True
            button_pressed=True
            first_move=True
            skip=False
            count=0
            while move and not interrupt: #ход
                for x in pygame.event.get(): #keyboard
                    if x.type == pygame.QUIT:
                        interrupt=True
                    if x.type==pygame.KEYDOWN:
                        first_move=True
                        if x.key==pygame.K_w or x.key==pygame.K_UP: 
                            ychanger=-1
                            button_pressed=True
                        if x.key==pygame.K_s or x.key==pygame.K_DOWN:  
                            ychanger=1
                            button_pressed=True
                        if x.key==pygame.K_d or x.key==pygame.K_RIGHT:  
                            xchanger=1
                            button_pressed=True
                        if x.key==pygame.K_a or x.key==pygame.K_LEFT:  
                            xchanger=-1
                            button_pressed=True
                        if x.key==pygame.K_SPACE:
                            if check_move():
                                territory[who_pl]=territory[who_pl]|sq(fig_size,fig_pos)
                                move=False
                                skip=False
                                score[who_pl]=len(territory[who_pl])-2
                        if x.key==pygame.K_LSHIFT or x.key==pygame.K_RSHIFT:
                            fig_size=[fig_size[1],fig_size[0]]
                            button_pressed=True
                        if x.key==pygame.K_f:
                            move=False
                            skip_counter+=1
                            skip=True
                    if x.type==pygame.KEYUP:
                        if x.key==pygame.K_w or x.key==pygame.K_s or x.key==pygame.K_UP or x.key==pygame.K_DOWN: 
                            ychanger=0
                            button_pressed=False
                        if x.key==pygame.K_d or x.key==pygame.K_a or x.key==pygame.K_RIGHT or x.key==pygame.K_LEFT: 
                            xchanger=0
                            button_pressed=False
                if button_pressed:
                    fill()
                    drawpixel(*corner[who_pl],pl_color)
                    if not first_move and count%5==0:
                        fig_move()
                    if first_move:
                        fig_move()
                    for t in range(players):
                        for m in territory[t]:
                            drawpixel(*m,colors[t])
                
                    drawrect(*fig_pos,*fig_size,pl_color2) #pl_color
                    grid()
                    text=font1.render(str(score[who_pl])+" + "+str(fig_square),1,(0,0,0))
                    screen.blit(text,(250,0))
                    
                count+=1
                pygame.display.update()
                clock.tick(30)
            if not skip:
                skip_counter=0
            who_pl=(who_pl+1)%players
        if not interrupt:
            gameover_screen()
        bug=True
        while bug and not interrupt:
            for x in pygame.event.get():
                if x.type==pygame.KEYDOWN:
                    bug=False
                if x.type == pygame.QUIT:
                    interrupt=True
            pygame.time.wait(20)
except:
    fill()
    grid()
    label="I don't know how,"
    text=font1.render(label,1,(0,0,0))
    screen.blit(text,(50,50))
    label="  but you've killed this game"
    text=font1.render(label,1,(0,0,0))
    screen.blit(text,(60,75))
    pygame.display.update()
    while not interrupt:
        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                interrupt=True
        pygame.time.wait(20)
pygame.quit()
sys.exit()
