import pygame

SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
FPS = 60
GRAVITY = 0.4

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False