# 录入学生信息
# 构造类
class Student:
    def __init__(self, name, age, addr):
        self.name = name  # 学生姓名
        self.age = age  # 学生年龄
        self.addr = addr  # 学生地址


# 通过for循环实现学生信息录入
for i in range(1, 11):
    print(f"当前录入第{i}位学生信息，总共需录入10位学生信息")
    stu = Student(
        input("请输入学生姓名:"),
        input("请输入学生年龄:"),
        input("请输入学生地址:")
    )
    print(f"学生{i}信息录入完成，信息为【学生姓名：{stu.name}，年龄：{stu.age}，地址：{stu.addr}】")