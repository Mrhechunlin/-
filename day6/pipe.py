from multiprocessing import Process,Pipe
import os,time

#创建管道对象
fd1,fd2=Pipe()

def fun(name):
    time.sleep(3)
    #向管道写如内容
    fd2.send("hello"+str(name))

jobs=[]
for i in range(5):
    p=Process(target=fun,args=(i,))#创建5个进程
    jobs.append(p)
    p.start()

    
for i in range(5):
    #读取管道
    data=fd1.recv()
    print(data)
for i in jobs:
    i.join()