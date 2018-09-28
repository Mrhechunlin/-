# -*- coding: utf-8 -*-
#!/usr/bin/ python3


'''
电子词典服务端

项目名称：电子词典

讲词典文本内容导入到数据库中

作者:何春林

QQ:243205112

邮箱：243205112@qq.com

日期：2018-09-28

'''

import pymysql
import re 

f=open("dict.txt")
db=pymysql.connect("localhost","root","123456","cidian")
cursor=db.cursor()
for line in f :
    l=re.split(r"\s+",line)
    word=l[0]
    interpret=" ".join(l[1:])
    sql="insert into words(word,interpret) values('%s','%s')"%(word,interpret)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
f.close()