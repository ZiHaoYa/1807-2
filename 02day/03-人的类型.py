class ren:
	def pao(self):
		print("跑")
	def chifan(self):
		print("吃饭")
	def youxi(self):
		print("打游戏")
	def introduce(self):
		print("我的年龄%d 我的身高%d"%(self.age,self.height))

suijingji = ren()
suijingji.pao()
suijingji.chifan()
suijingji.youxi()

suijingji.age = 21#添加属性
suijingji.height = 170#添加属性
suijingji.introduce()
print(suijingji.age)
print(suijingji.height)


