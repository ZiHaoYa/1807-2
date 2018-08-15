class che():
	def __init__(self,yanse,xinghao):
		self.yanse = yanse
		self.xinghao = xinghao
	def __str__(self):
		zh = "颜色%s,型号%s"%(self.yanse,self.xinghao)
		return zh



	def yinyue(self):
		print("听音乐")
	def yidong(self):
		print("移动")

mashaladi = che("蓝色","玛莎拉蒂")#创建一个车的对象
mashaladi.yinyue()
mashaladi.yidong()
print(mashaladi)
