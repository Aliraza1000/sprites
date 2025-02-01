import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangle Movment")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
player_rect = pygame.Rect(300, 250, 50, 50)
stationry_rect = pygame.Rect(500, 300, 50, 50)
speed = 5
running = True
while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.x > 0:
        player_rect.x -= speed
    if keys[pygame.K_RIGHT] and player_rect.x < WIDTH - player_rect.width:
        player_rect.x += speed
    if keys[pygame.K_UP] and player_rect.y > 0:
        player_rect.y -= speed
    if keys[pygame.K_DOWN] and player_rect.y < HEIGHT - player_rect.height:
        player_rect.y += speed
    screen.fill(WHITE)  
    pygame.draw.rect(screen, BLUE, player_rect)  
    pygame.draw.rect(screen, RED, stationary_rect) 

    pygame.display.update()
pygame.quit()