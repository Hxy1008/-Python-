def decorator(fn):
    def wrapper(*args, **kwargs):
        print("ON")
        fn(*args, **kwargs)
        print("OFF")
    return wrapper


@decorator
def play_lol(username, password, hero):
    print("lol", username, password, hero)


@decorator
def play_dnf(username, password):
    print("dnf", username, password)


play_lol('zhangsan', 3213213, hero='jax')
play_lol('lisi', 414124325, 'master yi')
play_dnf("wangwu", 72432784382)