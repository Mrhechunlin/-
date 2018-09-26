import signal

from time import sleep

signal.alarm(5) #５秒向自身发送时钟信号
#使用默认方法处理信号

# signal.signal(signal.SIGALRM,signal.SIG_DFL)

# #忽略信号
signal.signal(signal.SIGALRM,signal.SIG_IGN)
signal.signal(signal.SIGINT,signal.SIG_IGN)

while 1:
    sleep(0.5)
    print("等待时钟．．")


