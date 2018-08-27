from threading import Thread
import time
def work(i):
	num = 0
	time.sleep(i)
	num += 1
	print(num)
def work(i):
	num = 0
	time.sleep(i)
	nmu =+ 2
	print(num)
t =Thread(target=work,args=(3,))
t1 = Thread(target=work,args(5,))
t.start()

