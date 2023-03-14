'''
题目1
有如下的代码，定义了一个Python列表 变量
var1 = [ 33, ['我的名字', '黑羽白月'], 'hello world!']
请接下来写一行代码，打印出var1这个列表变量里面的 字符串 hello world!

题目2
有如下的代码，定义了一个Python列表 变量
var1 = [ 33, ['我的名字', '黑羽白月'], 'hello world!']
请接下来写一行代码，打印出var1这个列表变量里面的 人名字 黑羽白月

题目3
有如下的代码，定义了一个Python列表 变量
var1 = [ 33, ['我的名字', '黑羽白月'], 'hello world!']
请分别用一行代码，实现：
修改var1这个列表变量里面的 hello world！ 为 Oh my God!
修改var1这个列表变量里面的 人名字 黑羽白月 为 拜月童子

题目4
有如下的代码，定义了一个Python列表 变量
var1 = [ 33, ('我的名字', '黑羽白月'), 'hello world!']
请接下来写一行代码， 修改var1这个列表变量里面的 人名字 黑羽白月 为 拜月童子
'''
var1 = [ 33, ['我的名字', '黑羽白月'], 'hello world!']
print(var1[2])
print(var1[1][1])
var1[2] = 'Oh My God!'
print(var1[2])
var1[1][1] = '拜月童子'
print(var1[1][1])
print(var1)