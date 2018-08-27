from multiprocessing import Process
import time
def show(name):
	for i in range(10):
		timr.sleep(2)
		print(name)
p = Process(target=show,args=("割草",))
P.start()
time.sleep(3)
P.terminate()
print("吃喝玩乐")
