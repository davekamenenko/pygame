import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First")

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = FALSE


pygame.quit()