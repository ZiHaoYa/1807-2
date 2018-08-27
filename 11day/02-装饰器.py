def  w1(fun):
	def inner():
		print("检测登入")
		fun()
	return inner
def pay():
	print("支付宝")
pay()
