class DiGua():
	def __init__(self):
		self.status = "生的"
		self.times = 0
		self.zl = {}
	def __str__(self):
		msg = "我考的程度是%s"%self.status
		return msg+str(self.zl)
	def cook(self,time):
		self.times+=time
		if self.times >= 1 and self times <= 2:
			self.status = "生的"
		elif self.times >= 3 and self.times <= 5:
			self.status = "半生半熟"
		elif self.times >= 6 and self.times <= 8:
			self.status = "8分熟"
		elif self.times >= 9 andseif.times <= 12:
			self.status = "正好"
		elif self.times > 12:

		




digua = DiGua()
for i in range(5):
	DiGua.cook(random.randint(1,4)
	

