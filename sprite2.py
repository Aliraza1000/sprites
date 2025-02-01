import pygame
from random import randint

pygame.init()
w, h = 800, 600
scr = pygame.display.set_mode((w, h))
pygame.display.set_caption("Sprite Color Change")
rnd_clr = lambda: (randint(0, 255), randint(0, 255), randint(0, 255))
class Spr(pygame.sprite.Sprite):
    def _init_(s, x, y):
        super()._init_()
        s.image = pygame.Surface((50, 50))
        s.rect = s.image.get_rect(topleft=(x, y))
        s.chg_clr()

    def chg_clr(s):
        s.image.fill(rnd_clr())
sp1, sp2 = Spr(300, 250), Spr(500, 300)
all_spr = pygame.sprite.Group(sp1, sp2)
CHG_CLR = pygame.USEREVENT + 1
pygame.time.set_timer(CHG_CLR, 1000)
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == CHG_CLR:
            for s in all_spr:
                s.chg_clr()
    scr.fill((255, 255, 255))
    all_spr.draw(scr)
    pygame.display.update()

pygame.quit()