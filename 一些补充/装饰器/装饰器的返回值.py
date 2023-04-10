def decorator(fn):
    def wrapper(*args, **kwargs):
        print("ON")
        result = fn(*args, **kwargs)
        print("OFF")
        return result
    return wrapper


@decorator
def play_lol(username, password, hero):
    print("lol", username, password, hero)


@decorator
def play_dnf(username, password):
    print("dnf", username, password)
    return '爆了一把屠龙刀'

result = play_dnf('zhangsan', 13213214)
print(result)