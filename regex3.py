import re 


s="""hello world
hello kitty
你好啊,北京"""
pattern=r'''H\w+
\s+
[a-z]+'''

regex=re.compile(pattern,flags=re.X|re.I)
try:
    s=regex.search(s).group()
except:
    print("没有匹配到内容")
else:
    print(s)