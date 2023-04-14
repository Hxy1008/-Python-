import hashlib

obj = hashlib.md5()
obj.update("424324".encode("utf-8"))
mi = obj.hexdigest()
print(mi)


obj = hashlib.md5("afdsafds3243245432".encode("utf-8"))
obj.update("424324".encode("utf-8"))
mi = obj.hexdigest()
print(mi)


def hashs(salt, s):
    obj = hashlib.md5(salt.encode("utf-8"))
    obj.update(s.encode("utf-8"))
    return obj.hexdigest()



# 用户注册

username = input("请输入用户名")
password = input("请输入密码")
mi_password = hashs(username, password)
f = open("06.user.txt", mode="w", encoding="utf-8")
f.write(username)
f.write("\n")
f.write(mi_password)
f.write("\n")
f.close()

# 登录

username = input("username:")
password = input("password:")
f = open("06.user.txt", "r", encoding="utf-8")
uname = f.readline().strip() # 因为加了换行符
upwd = f.readline().strip()
if username == uname and upwd == hashs(username, password):
    print("登录成功")
else:
    print("用户名密码输入错误")
