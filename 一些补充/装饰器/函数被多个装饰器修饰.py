def decorator1(fn):
    def wrapper(*args, **kwargs):
        print("这里是装饰器1，进入")
        result = fn(*args, **kwargs)
        print("这里是装饰器2，结束")
        return result
    return wrapper


def decorator2(fn):
    def wrapper(*args, **kwargs):
        print("这里是装饰器2，进入")
        result = fn(*args, **kwargs)
        print("这里是装饰器2，结束")
        return result
    return wrapper


@decorator1
@decorator2
def test(a, b):
    print("这里是目标函数")
    return a + b


result = test(1, 2)
print(result)