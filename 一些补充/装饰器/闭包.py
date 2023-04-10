'''
闭包:
    1. 可以让一个变量常驻于内存
    2. 避免全局变量被污染
'''


def func():
    a = 10
    def func2():
        nonlocal a
        a += 1
        return a
    return func2  #func2即为一个闭包函数


r1 = func()
a1 = r1()
a2 = r1() # 这样字，实现了在外部操作函数内部的局部变量
print(a1, a2)