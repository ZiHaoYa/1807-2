from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.connect(("192.168.43.66",8080))
s.send("社会让你呼风唤雨 是我刘美丽配不上你".encode("gb2312"))
while True:
	msg = s.recv(1024).decode("gb2312")
	print(msg)
