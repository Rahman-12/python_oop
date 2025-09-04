import pygame


class Player:
    def __init__(self, x, y, width=50, height=30, speed=5):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.move(-self.speed, 0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.move(self.speed, 0)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        # Keep inside screen
        self.rect.x = max(0, min(self.rect.x, 1280 - self.rect.width))

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), self.rect)
