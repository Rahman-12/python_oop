import pygame
from player import Player

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Create player
player = Player(1280//2 - 25, 720 - 50)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.handle_input()

    screen.fill((0, 0, 0))
    player.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
