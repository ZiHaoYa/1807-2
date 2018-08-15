list = []#先定义一个空列表
def add():#添加函数功能
	dic = {}#定义一个空字典
	name = input("姓名:")
	sex = input("性别:")
	mz = input("名族:")
	cs = input("出生:")
	zz = input("住址:")
	zzh = input("身份证号:")
	dic["name"]=name
	dic["sex"]=sex
	dic["mz"]=mz
	dic["cs"]=cs
	dic["zz"]=zz
	dic["zzh"]=zzh
	list.append(dic)
	print("恭喜你添加添加成功")
def cat():
	name = input("请输入你要查找的姓名:")
	flag = False
	for i in list:
		if i["name"]==name:
			print(i)
			flag = True
	if flag == False:
		print("查无此人")
def delete():
	name = input("输入姓名")
	flag = False
	for position,i in enumerate(list):
		if i["name"]==name:
			list.pop(position)
			flag = True
	if flag == False:
		print("查无此人")
def change():
	name = input("输入姓名")
	flag = False
	for i in list:
		if i["name"]== name :
			i["name"]=input("输入新的名字")
			i["sex"]=input("输入性别")
			i["mz"]=input("民族")
			i["cs"]=input("出生")
			i["zz"]=input("住址")
			i["zzh"]=input("身份证号")
			flag = True
	if flag == False:
		print("查无此人")
while True:
	print("欢迎使用身份证管理系统".center(70,"*"))
	print(" ")
	function = int(input(" 1.请输入你要添加的名字\n 2.请输入你要查看的名字\n 3.请输入你要修改的名字\n 4.请输入你要删除的名字\n 5.退出系统\n\n 请选择功能:"))
	if function == 1:
		print("请认真填写".center(72,"*"))
		add()
	elif function == 2:
		print("请认真填写".center(72,"*"))
		cat()
	elif function == 3:
		print("请认真填写".center(72,"*"))
		change()
	elif function == 4:
		print("请认真填写".center(72,"*"))
		delete()
	elif function == 5:
		print("欢迎下次使用".center(72,"*"))
		break
