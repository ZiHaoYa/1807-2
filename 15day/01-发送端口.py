from socket import *
s = socket(AF_INET,SOCK_DGRAM)
m = input("请输入发送的数据")
s.sendto("乖 快 隋静听话 叫爸爸 哈哈哈哈哈!".encode("gb2312"),("192.168.43.66",8080))
r = s.recvfrom(1024)
print(r[0].decode("gb2312"))
print(r[1][0])
print(r[1][1])
s.close()

