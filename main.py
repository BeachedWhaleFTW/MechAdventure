import pygame

import classes

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

black = 0, 0, 0
white = 255, 255, 255

fps = 60
clock = pygame.time.Clock()

player = classes.Player()

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game_running = False

    player.handle_keys()

    screen.fill(white)
    player.draw(screen)
    pygame.display.update()

    clock.tick(fps)
