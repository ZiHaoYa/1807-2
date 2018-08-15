class gou():
	def __init__(self,name):
		self.name = name



class zhu(gou):
	pass
class che(gou):
	pass


suijing = gou("哈士奇")
print(suijing.name)
yezhu = zhu("隋静")
print(yezhu.name)
falali = che("法拉利")
print(falali.name)
