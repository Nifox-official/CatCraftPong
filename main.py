from pygame import *
from random import *
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
            score_r +=1
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
ball.direct[0]= choice([-1,1])
ball.direct[1]= choice([-1,1])
mixer.init()
mixer.music.load('music.mp3')
mixer.music.play(-1)
clock = time.Clock()
fps=60
score_l=0
score_r=0
rule = 3
game = True
finish=True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.blit(background, (0,0))
    player1.reset()
    player1.update_left()
    player2.reset()
    player2.update_right()
    ball.reset()
    ball.update()

    display.update()
    clock.tick(fps)
