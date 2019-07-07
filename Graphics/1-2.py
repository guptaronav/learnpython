import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

BLACK = [0, 0, 0]

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game") 
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
