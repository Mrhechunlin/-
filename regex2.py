import re

pattern=r"(?P<jire>ab)cd(?P<maomao>ef)"
regex=re.compile(pattern)

#获取match对象
math_obj=regex.search("sdaabcdefghij")

print(math_obj.pos)
print(math_obj.endpos)
print(math_obj.re)
print(math_obj.string)
print(math_obj.lastgroup)
print(math_obj.lastindex)
print("================")

print(math_obj.start())
print(math_obj.end())
print(math_obj.span())
print(math_obj.group("maomao"))
print(math_obj.groupdict())
print(math_obj.groups())