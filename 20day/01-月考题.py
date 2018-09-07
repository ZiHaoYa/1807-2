import time
list = [] 
lists = []
def choose():
		while True:
			print("欢迎来到酒店管理系统")
			print("入住 1")
			print("离店 2")
			print("统计 3")
			print("退出 4")
			gn()
def gn():
	gn = int(input("请选择功能:"))
	if gn == 1:
		add()
	elif gn == 2:
		li()
	elif gn == 3:
		tj()
	elif gn == 4:
		tc()
	else:
		print("选择有误")

def add():
	d = {}
	name = input("请输入名字")
	a["name"] = name
	list.append(d)
def li():
	d = {}
	name = input("请输入名字")
	a = time.time

	d["name"] = name
	lists.append(d)
def tj():
	money =(t1-t)*10
	print("总共花费%s"%money)
	peple = len(list)
	print("总人数为%d"%peple)
def tc():
	

choose()
