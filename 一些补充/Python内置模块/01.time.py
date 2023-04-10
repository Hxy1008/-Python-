import time
"""
time.sleep() 休眠
time.time()
"""
print("hello")
time.sleep(3)
print("你好")

# while True:
#     print("抓取信息")
#     time.sleep(1)
a = time.time()
start = time.time()
for i in range(500):
    print(i)
end = time.time()
print(f'{end - start}')
