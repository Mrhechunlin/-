from multiprocessing import Pool
import time

def fun(n):
    time.sleep(1)
    print("执行pool map 事件")
    return n*n

pool=Pool(4)
r=pool.map(fun,range(10))
pool.close()
pool.join()
print(r)