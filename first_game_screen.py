import pygame
pygame.init()
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption('My Awesome Game')
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
pygame.display.flip()