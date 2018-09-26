from multiprocessing import Process
from time import sleep


#带参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working...")

p=Process(target=worker,args=(2,"zhang"),name='hechunlin')
p.start()
print("process name:",p.name) #进程名称
print("process pid:",p.pid) #获取进程PID
print("process is alive:",p.is_alive())
p.join(1)
print("====================")

print("process is alive:",p.is_alive())
