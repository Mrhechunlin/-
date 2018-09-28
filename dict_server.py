# -*- coding: utf-8 -*-
#!/usr/bin/ python3


'''
电子词典服务端

项目名称：电子词典

相关技术：多进程，Mysql等

作者:何春林

QQ:243205112

邮箱：243205112@qq.com

日期：2018-09-28

'''

from socket import *
import os
import time
import signal
import pymysql
import sys

#定义需要的全局变量
DICT_text="./dict.txt"
HOST="0.0.0.0"
PORT=8000
ADDR=(HOST,PORT)

#主要的流程控制
def main():
    #创建数据库链接
    db=pymysql.connect("localhost","root","123456","cidian")
    #创建套接字
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    #忽略子进程信号
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    while True:
        try:
            c,addr=s.accept()
            print("连接来自",addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务器退出")            
        except Exception as e:
            print(e)
            continue
        #创建子进程
        pid=os.fork()
        if pid==0:
            s.close()
            do_child(c,db)
        else:
            c.close()
            continue

def do_child(c,db):
    while 1:
        date=c.recv(1024).decode()
        print(c.getpeername(),":",date)
        if (not date) or date[0]=="E":#接收开头字母为E时，退出
            c.close()
            sys.exit("推出")
        elif date[0]=="R":#接收开头字母为R时,执行操作函数
            do_register(c,db,date)
        elif date[0]=="L":#接收开头字母为L时,执行登录函数
            do_login(c,db,date)
        elif date[0]=="Q":#接收开头字母为Q时，执行查询函数
            do_query(c,db,date)
        elif date[0]=="H":#接收开头字母为H时,执行历史记录操作
            do_hist(c,db,date)

def do_register(c,db,date):
    print("注册操作")
    l=date.split(" ")
    name=l[1]
    passwd=l[2]
    cursor=db.cursor()
    sql="select * from user where name='%s'"%name
    cursor.execute(sql)
    r=cursor.fetchone()
    if r != None:
        c.send(b"NO")
        return
    sql="insert into user(name,passwd) values ('%s','%s')"%(name,passwd)
    try:
        cursor.execute(sql)
        db.commit()
        c.send(b"OK")
    except:
        db.rollback()
        c.send(b"Fall")
    else:
        print("%s注册成功"%name)

def do_login(c,db,date):
    print("登录操作")
    l=date.split(" ")
    name=l[1]
    passwd=l[2]
    cursor=db.cursor()

    sql="select * from user where name='%s' and passwd='%s'"%(name,passwd)
    cursor.execute(sql)
    r=cursor.fetchone()
    if r==None:
        c.send(b"NO")
    else:
        print("%s登录成功"%name)
        c.send(b"OK")
    


def do_query(c,db,data):
    print("查询操作")
    l=data.split(" ")
    name=l[1]
    word=l[2]
    cursor=db.cursor()
    def insert_history():
        tm=time.ctime()
        sql="insert into hist(name,word,time) values('%s','%s','%s')"%(name,word,tm)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()


    
    try:
        cursor.execute('select *from words where word = "%s"' % word)
        date=cursor.fetchall()
        if date:
            c.send(b"OK")
            time.sleep(0.1)
            c.send(date[0][2].encode())
            insert_history()
        else:
            c.send(b"FALL")
        db.commit()
    except Exception as e:
        print(e)


def do_hist(c,db,data):
    print("历史记录")
    l=data.split(" ")
    name=l[1]
    cursor=db.cursor()
    sql="select * from hist where name='%s'"%name
    cursor.execute(sql)
    r=cursor.fetchall()
    if not r:
        c.send(b"FALL")
        return
    else:
        c.send(b"OK")
    for i in r :
        time.sleep(0.1)
        msg="%s  %s   %s"%(i[1],i[2],i[3])
        c.send(msg.encode())
    time.sleep(0.1)
    c.send(b"##")


    
if __name__ == '__main__':
    main()