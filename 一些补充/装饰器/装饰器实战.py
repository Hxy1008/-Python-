# 员工信息管理系统
login_flag = 0


def decorator(fn):
    def wrapper(*args, **kwargs):
        global login_flag
        if login_flag == 0:
            while True:
                print('请登录：')
                username = input('>>>')
                password = input('>>>')
                if username == "admin" and int(password) == 123456:
                    print("登录成功")
                    login_flag = 1
                    break
                else:
                    print('登录失败,用户名或密码错误，请重新登录')
                    continue
        result = fn()
        return result
    return wrapper


@decorator
def add():
    print("添加员工信息")


@decorator
def update():
    print("修改员工信息")


@decorator
def insert():
    print("插入员工信息")


@decorator
def delete():
    print("删除员工信息")


@decorator
def search():
    print("查找员工信息")


add()
update()
