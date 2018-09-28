# -*- coding: utf-8 -*-
#!/usr/bin/ python3


'''
电子词典客户端

项目名称：电子词典

相关技术：Mysql等

作者:何春林

QQ:243205112

邮箱：243205112@qq.com

日期：2018-09-28

'''

from socket import *
import sys
import getpass


#创建网络连接
def main():
    if len(sys.argv)<3:
        print("argv is error")
        return 
    HOST=sys.argv[1]
    PORT=int(sys.argv[2])
    s=socket()
    try:
        s.connect((HOST,PORT))
    except Exception as e:
        print(e)
        return
    while True:
        print('''
            ==========Welcome===========
            -- 1.注册  2.登录　 3.退出--
            ============================
            ''')
        try:
            cmd=int(input("请输入选项:"))
        except Exception as e:
            print("命令错误")
            continue
        if cmd not in [1,2,3]:
            print("请输入正确选项")
            sys.stdin.flush()
            continue
        elif cmd==1:
            r=do_zhuce(s)
            if r==0:
                print("注册成功")
               
            elif r==1:
                print("用户存在")
            else:
                print("注册失败")
        elif cmd==2:
            name=do_login(s)
            if name:
                print("登录成功")
                login(s,name)
            else:
                print("用户名和密码不正确")
        elif cmd==3:
            s.send(b"E")
            sys.exit("谢谢使用")

def do_zhuce(s):
    while 1:
        name=input("user:")
        passwd=getpass.getpass("passwd:")
        passwd1=getpass.getpass("again:")
        if (" "in name) or (" "in passwd):
            print("用户名和密码不能有空格")
            continue
        if passwd != passwd1:
            print("两次密码不一致")
            continue
        msg="R {} {}".format(name,passwd)
        s.send(msg.encode())
        data=s.recv(1024).decode()
        if data =="OK":
            return 0
        elif data=="NO":
            return 1
        else:
            return 2

def do_login(s):
    name=input("user:")
    passwd=getpass.getpass("passwd:")
    msg="L {} {}".format(name,passwd)
    s.send(msg.encode())
    data=s.recv(128).decode()
    if data=="OK":
        return name
    else:
        return 
    
def login(s,name):
    while 1:
        print('''
            ========查询界面================
            1. 查词　　2.历史记录　3.退出
            ===============================
            ''')
        try:
            cmd=int(input("请输入选项:"))
        except Exception as e:
            print("命令错误")
            continue
        if cmd not in [1,2,3]:
            print("请输入正确选项")
            sys.stdin.flush()
            continue
        elif cmd==1:
            do_query(s,name)
        elif cmd==2:
            do_hist(s,name)
        elif cmd==3:
            return
def do_query(s,name):
    while True:
        word=input("输入单词:")
        if word=="##":
            break
        msg="Q {} {}".format(name,word)
        s.send(msg.encode())
        date=s.recv(128).decode()
        if date=="OK":
            date=s.recv(2048).decode()
            print(date)
        else:
            print("没有查到该单词")

def do_hist(s,name):
    msg="H {}".format(name)
    s.send(msg.encode())
    date=s.recv(128).decode()
    if date=="OK":
        while True:
            date=s.recv(1024).decode()
            if date=="##":
                break
            print(date)
    else:
        print("没有历史记录")

if __name__ == '__main__':
    main()