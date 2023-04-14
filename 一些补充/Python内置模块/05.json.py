import json
dic = {"id": 1, "name": "admin", "usertype": 0, "我测你们码": "理塘dj"}
s = json.dumps(dic, ensure_ascii=False)
print(s, type(s))
dic1 = json.loads(s)
print(dic1, type(dic1))