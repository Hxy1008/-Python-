a = 10
def func1():
    global a
    print(a)
    a = 20
    print(a)
    b = 10
    def func2():
        nonlocal b # 向外找一层，找到就引入 不然就再向外一层、直到找到 但只能找局部变量，不能找全局变量
        print(b)
    func2()

func1()
print(a)