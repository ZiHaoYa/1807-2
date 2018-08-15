class ren:
	def __init__(self,name):
		self.name = name
	def zhuangzidan(self,dj,zd):
		dj.addzidan(zd)
	def zhuangdanjia(self,dj,gun):
		gun.adddanjia(dj)



class qiang():
	def __init__(self,name):
		self.name = name



class danjia():
	def __init__(self,count):
		self.count = count
		self.zds =[]
	def addzidan(self,zd):
		self.zds.append(zd)


class zidan():
	def __init__(self,name,sh):
		self.name = name
		self.sh = sh



laowang = ren("老王")
AK47 = qiang("AK47")
dj = danjia(40)
for i in range(40):
	zd = zidan("7.62",5)
	laowang.zhuangzidan(dj,zd)
laowang.zhuangdanjia(AK47,dj)
