from pygame import *
from random import randint
from time import time as timer

back = (200, 255, 255) 
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

display.set_caption("Пинг-Понг")
background = transform.scale(image.load("background.png"), (win_width, win_height))

game = True

clock = time.Clock()
FPS = 60

speed = 5

racket = 'racket.png'
tenis_ball = 'tenis_ball.png'

lost = 0
score = 0

#mixer.init()
#mixer.music.load('space.ogg')
#fire_sound = mixer.Sound('fire.ogg')
#mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 354:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 354:
            self.rect.y += self.speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        #global lost
        #if self.rect.y > win_height:
           #self.rect.y = 0
            #self.rect.x = randint(80, win_width - 80)


#balls = sprite.Group()

racket1 = Player('racket.png', 30, 200, 4, 50, 150) 
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 275, 225, 4, 50, 50)

#font.init()
#font1 = font.SysFont('Arial', 40)

#font.init()
#font = font.SysFont('Arial', 70)

#winfin = font.render(
#    'YOU WIN!', True, (255, 255, 0)
#)
#fail = font.render(
#    'YOU LOSE!', True, (255, 0, 0)
#)
#bullet_reload = font1.render(
#    'Погодь...перезагрузка 3 сек', True, (255, 255, 255)
#)

finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0,0))
        #lose = font1.render(
            #'Пропущено:' + str(lost), True, (255, 255, 255)
        #)
        #win = font1.render(
            #'Сбито:'+ str(score), True, (255, 255, 255)
        #)

        racket1.update_l()
        racket1.reset()
        racket2.update_r()
        racket2.reset()
        ball.reset()

        #window.blit(win, (10, 20))
        #window.blit(lose, (10, 50))
        #collides = sprite.groupcollide(monsters, bullets, True, True)
        #sprites_list_monster = sprite.spritecollide(ship, monsters, False)
        #sprites_list_aster = sprite.spritecollide(ship, asteroids, False)

        #for collide in collides:
            #monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 3))
            #monsters.add(monster)
            #score += 1
        
        #if score >= 10:
            #window.blit(winfin, (200, 200))
            #finish = True

        #if lost >= 3 or sprites_list_monster or sprites_list_aster:
            #window.blit(fail, (200, 200))
            #finish = True
            
        display.update()

    clock.tick(FPS)