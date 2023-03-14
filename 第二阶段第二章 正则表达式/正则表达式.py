import re
'''
# 匹配一个.com邮箱格式的字符串
re.findall(r'\w+@\w+\.com', 123456789@qq.com)
# 匹配一个密码8-12位数字字母下划线构成
re.findall(r'[_0-9a-zA-Z]{8,12}', 'ewqe_1234')
# 匹配数字，包括正数，复数，小数，分数，百分数
re.findall(r'-?\d+\.?/?\d*%?', '12, -3, 3.5, -4.5, 1/2, 45%')
# 匹配文字中以大写字母开头的单词
re.findall(r'\b[A-Z][-_a-zA-Z]*', 'Hello, iPython H-base HAPPY ')
'''
a = re.findall(r'\b[A-Z][-_a-zA-Z]*', 'Hello, iPython H-base HAPPY ')
print(a)