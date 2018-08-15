import pygame
pygame.init()
zh = pygame.Rect(100, 500, 120, 126)
zzh = pygame.display.set_mode((480, 700))
bg = pygame.image.load("./images/background.png")
zzh.blit(bg,(0,0))
pygame.display.update()
while True:
	pass
pygame.quit()

