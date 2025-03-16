from pygame import *
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

window=display.set_mode((700,500))
display.set_caption('Ping Pong')
background = transform.scale(image.load('backround.png'),(700 ,500))
player=Player('left_cat.png', 250,400,100,100,5)
mixer.init()
mixer.music.load('music.mp3')
mixer.music.play(0)
clock = time.Clock()
fps=60


game = True
finish=True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.blit(background, (0,0))
    player.reset()
    player.update_left()



    display.update()
    clock.tick(fps)
