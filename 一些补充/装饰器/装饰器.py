def decorator(fn):
    def wrapper():
        print("ON")
        fn()
        print("OFF")
    return wrapper


@decorator
def play_lol():
    print("lol")


play_lol()
