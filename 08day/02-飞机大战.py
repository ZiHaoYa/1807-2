import pygame
pygame.init()

screen = pygame.display.set_mode((480, 700))#创建游戏主窗口


bg = pygame.image.load("./images/background.png")#绘制背景图 加载图像
screen.blit(bg, (0, 0))#绘制在屏幕
#pygame.display.update()#更新显示


hero=pygame.image.load('./images/hero.gif')#加载图像
screen.blit(hero,(200,500))#绘制屏幕的什么位置
pygame.display.update()#更新显示


clock=pygame.time.Clock()#创建游戏时钟对象
#i=0#创建游戏时钟对象


hero_rect=pygame.Rect(200,500,102,126)#定义英雄的初始位置
enemy = EnemySprite()
enemy = EnemySprite()
enemy1.rect.x = 50
enemy1.rect.y = 700
enemy1.speed = -2
enemy_group = pygame.sprite.Group(enemy,enemy)
while True:#游戏循环
	clock.tick(60)#一秒刷新60次
	hero_rect.y-=5#相当速度
	screen.blit(bg,(0,0))
	screen.blit(hero, hero_rect)

	if hero_rect.bottom<=0: #如果移除屏幕
		hero_rect.top=700 #则英雄的顶部移动到屏幕底部

	enemy_group.update()
	enmey_group.draw(scteen)
'''
	for event in pygame.event.get():

	# 判断用户是否点击了关闭按钮
	if event.type == pygame.QUIT:
	print("退出游戏...")

pygame.quit()

# 直接退出系统
exit()
'''
#	pygame.display.update()


#while True:#游戏循环
#	pass
pygame.quit()#更新显示

