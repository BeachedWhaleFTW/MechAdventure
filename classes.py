import pygame


class Player(object):
    def __init__(self):
        self.image = pygame.image.load('images/player.png')
        self.x = 0
        self.y = 0

        self.speed = 2

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_s]:
            self.y += self.speed
        elif key[pygame.K_w]:
            self.y -= self.speed
        elif key[pygame.K_d]:
            self.x += self.speed
        elif key[pygame.K_a]:
            self.x -= self.speed

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
