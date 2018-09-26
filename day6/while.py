import os
from time import sleep,ctime
while 1:
    sleep(3)
    print(ctime(),os.getpid())