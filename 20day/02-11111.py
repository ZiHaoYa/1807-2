'''
for i in range(1,10):
	for j in range(1,10):
		x = i*j
		print("%d*%d=%d"%(i,j,x))
'''


def w1(fun)
	def a():
		print("正在验证")
		fun()
	return a
@w1
def Test():
	print("哈哈")
Test()
