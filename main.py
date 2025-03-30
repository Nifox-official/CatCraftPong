from pygame import *
from random import *
import time as timer
class GameSprite(sprite.Sprite):
    def __init__(self, img,x,y,w,h,speed):
        super().__init__()
        self.image=transform.scale(image.load(img),(w,h))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.speed=speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)

class Player(GameSprite):
    def update_left(self):
        key_pressed=key.get_pressed()
        if key_pressed[K_w]and self.rect.y>0:
            self.rect.y -= self.speed
        if key_pressed[K_s]and self.rect.y<400:
            self.rect.y += self.speed
    def update_right(self):
        key_pressed=key.get_pressed()
        if key_pressed[K_UP]and self.rect.y>0:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN]and self.rect.y<400:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, img,x,y,w,h,speed):
        super().__init__(img,x,y,w,h,speed)
        self.direct = [0,0]
    def update(self):
        global score_l,score_r
        self.rect.x += self.speed*self.direct[0]
        self.rect.y += self.speed*self.direct[1]
        if self.rect.y <= 0 or self.rect.y>=500-self.rect.height:
            self.direct[1]*= -1
        # if self.rect.x <= 0 or self.rect.x>=700-self.rect.height:
        #     self.direct[0]*= -1
        if self.rect.colliderect(player1) or self.rect.colliderect(player2):
            self.direct[0]*= -1
        if self.rect.x<=0:
            score_r +=1
            self.start()
        if self.rect.x>=700-self.rect.width:
            score_l +=1
            self.start()
        

    def start(self):
        self.rect.x = 310
        self.rect.y = 210
        ball.direct[0]= choice([-1,1])
        ball.direct[1]= choice([-1,1])

window=display.set_mode((700,500))
display.set_caption('Cat Pong')
background = transform.scale(image.load('backround.png'),(700 ,500))
player1=Player('left_cat.png', 0,200,100,100,5)
player2=Player('right_cat.png', 600,200,100,100,5)
ball=Ball('ball.png', 350-40,250-40,80,80,5)
btn_play=GameSprite('play.png', 200,250,300,200,0)
logo=GameSprite('logo.png', 70, 100,600,200,0)
ball.direct[0]= choice([-1,1])
ball.direct[1]= choice([-1,1])
mixer.init()
mixer.music.load('music.mp3')
mixer.music.play(-1)
clock = time.Clock()
font.init()
font_1=font.SysFont('Arial',36)
fps=60
score_l=0
score_r=0
rule = 3
game = True
finish=True
menu=True
win=''

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    
    if menu:
        window.blit(background, (0,0))

        pressed=mouse.get_pressed()
        pos=mouse.get_pos()
        if pressed[0]:
            if btn_play.rect.collidepoint(pos[0],pos[1]):
                menu=False
                finish=False
        if win != '':
            winner = font_1.render('Победил'+win+'!',1,(255,255,255))
            scr=font_1.render('Со счётом '+str(max(score_l,score_r))+':'+str(min(score_l,score_r)),1,(255,255,255))
            window.blit(winner,(100,250))
            window.blit(scr,(100,300))
            display.update()
            timer.sleep(4)
            win=''
            score_l=0
            score_r=0
        btn_play.reset()
        logo.reset()

    if not finish:
        window.blit(background, (0,0))
        player1.reset()
        player1.update_left()
        player2.reset()
        player2.update_right()
        ball.reset()
        ball.update()
        score_1=font_1.render(str(score_l),1,(255,255,255))
        score_2=font_1.render(str(score_r),1,(255,255,255))
        window.blit(score_1,(50,50))
        window.blit(score_2,(650,50))
        if score_l>=5:
            win=' Левый чувак'
            finish=True
            menu=True
        if score_r>=5:
            win=' Правый чувак'
            finish=True
            menu=True

    display.update()
    clock.tick(fps)
