def show():
	for i in range(10):
		timr.sleep(10000
		print("哈哈哈")
p = Pool()#创建一个池子，可以装无限个进程
for i in range(3):
	p.apply_async(show)
	print("添加成功")
p.close()#关闭池子
p.join()#不支持传超时间
print("呵呵呵")
