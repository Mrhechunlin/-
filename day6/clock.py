from multiprocessing import Process
import time

class ClockProcess(Process):
    def __init__(self,value):
        self.value=value
        super().__init__()
    #重写run方法
    def run(self):
        for i in range(5):
            print("the time in {}".format(time.ctime()))
            time.sleep(self.value)
#创建自定义进程类　的对象
p=ClockProcess(2)

#调用run 方法
p.start()
p.join()