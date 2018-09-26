from multiprocessing import Process,Value
import time
import random
money=Value("i",2000)#创建共享内存

def deposite():
    for i in range(100):
        time.sleep(0.05)
        # 对value属性操作即操做共享内存数据
        money.value+=random.randint(1,200)

def shopping():
    for i in range(100):
        time.sleep(0.04)
        money.value-=random.randint(1,180)

d=Process(target=deposite)
w=Process(target=shopping)
d.start()
w.start()
d.join()
w.join()
print(money.value)
