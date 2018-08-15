class jiandaobu:
	def jiandao(self):
		import random
		i = 0
		while i < 3:
			pc = random.randint(1,3)
			py =int(input("请输入1:石头2:剪刀3:布"))
			if py >0 and py < 4:
				if (py == 1 and pc == 2) or (py == 2 and pc == 3) or (py == 3 and pc == 1 ):
					print("玩家赢了")
				elif py == pc:
					print("平局")
				else:
					print("电脑赢了")
			else:
				print("输入有误")
			i+=1
z = jiandaobu()
z.jiandao()
