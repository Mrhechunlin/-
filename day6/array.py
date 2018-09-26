from multiprocessing import Process,Array
import time

#创建共享内存，初始放入列表
# shm=Array('i',[1,2,3,4,5])
#创建共享内存，开辟五个整形空间
# shm=Array('i',5)
#存入字符串　要求是bytes格式
shm=Array('c',b'hello world')
def fun():
    for i in shm:
        print(i.decode())
    shm[0]=b'H'#子进程更改内存中的信息

p=Process(target=fun)
p.start()
p.join()

for i in shm:
    print(i.decode())#父进程
print(shm.value)#打印字符串