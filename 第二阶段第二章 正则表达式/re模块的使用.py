'''
regex.py re模块 功能函数演示
'''
import re
# 目标字符串
s = 'Alex:1994,Sunny:1996'
pattern = r'\w+:\d+'
# findall
    # re模块直接调用findall
l = re.findall(pattern, s)
print(l)
    # 使用compile对象调用findall
regex = re.compile(pattern)
l = regex.findall(s)
print(l)
# split
    # 使用re模块直接调用split
l = re.split(r'[:,]', s)
print(l)
    # 使用compile对象调用split
regex = re.compile('[:,]')
l = regex.split(s)
print(l)
# sub
s = re.sub(r':', '-', s)
print(s)
'''
生成match对象的函数
'''
s = '今年是2019年，建国70周年'
pattern = r'\d+'
# re.finditer()
it = re.finditer(pattern, s)
for i in it:
    print(i)
# re.fullmatch()完全匹配
it = re.fullmatch(r'[，\w]+', s)
print(it.group())
# re.match() 匹配开头位置
it = re.match('\w+', s)
print(it.group())
# re.search 匹配第一处符合正则表达式的位置
it = re.search('\d+', s)
print(it.group())