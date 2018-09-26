import re

it=re.finditer(r"\d+","2008-2018 10年，中国发生改100地的神级变化术")


for i in it:
    print(i.group())
try:
    obj=re.fullmatch(r"\w+","abcdef123")
    print(obj.group())

except AttributeError as e:
    print(e)

obj=re.match(r'foo',"foo food on the table")
print(obj.group())

obj=re.search(r'foo',"Foo food on the table")
print(obj.group())