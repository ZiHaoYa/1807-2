import pygame

class GameSprite(pygame.sprite.Spritr):
	def __init__()self,imagename,speed=1):
		super().__init__()
		self.image = pygame.image.load(imagen)
		self.rect = self.image.get_rect()
		self.speed = speed

	def update(self):
		self.rect.y+=self.speed



class EnemySprite(GameSPrite):
	def __init__(self):
		self.imagename = "./images/enemy0.png"
		super().__init__(self.imagename)
	def update(self):
		super().update()