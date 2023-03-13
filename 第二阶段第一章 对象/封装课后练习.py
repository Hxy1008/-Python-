# 封装课后练习
# 定义手机类
class Phone:
    __is_5g_enable = False  # 5G默认关闭

    def __check_5g(self):
        if self.__is_5g_enable:  # if self.__is_5g_enable == True:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")

    def call_by_5g(self):
        self.__is_5g_enable = True
        self.__check_5g()
        print("正在通话中")

    def call_by_4g(self):
        self.__is_5g_enable = False
        self.__check_5g()
        print("正在通话中")


phone = Phone()  # 构造一个Phone对象
phone.call_by_5g()  # 调用call_by_5g方法
