import os
from multiprocessing import Process as Po

filename='./send.jpg'
#获取文件大小
size=os.path.getsize(filename)

# 如果子进程使用父进程的对象，那么相互之间有偏移量的影响
# f= open(filename,'rb')


def copy1():
    f= open(filename,'rb')
    n=size//2
    fw=open("file.jpg","wb")

    while 1:
        if n<1024:
            data =f.read(n)
            fw.write(data)
            break
        data=f.read(1024)
        fw.write(data)
        n-=1024
    f.close()
    fw.close()

def copy2():
    f=open(filename,"rb")
    fw=open("file1.jpg","wb")
    f.seek(size//2,0)
    while 1:
        data=f.read(1024)
        if not data:
            break
        fw.write(data)
    f.close()
    fw.close()

p1=Po(target=copy1)
p2=Po(target=copy2)
p1.start()
p2.start()
print(p1.pid)
p1.join()
p2.join()


