name = input("请输入备份名称")
f = open(name,"r")
content = f.read()

fi = open("备份.txt","w")
fi.write(content)
f.close
fi.close
