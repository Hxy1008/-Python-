import random
seed = random.random()
print(random.uniform(5,9))
print(random.randint(3,20))
ls = ['1','2','3','4','5','6','7','8','9','0']
print(random.choice(ls))
print(random.sample(ls, 3))


def rand_num():
    return str(random.randint(0, 9))


def rand_upper():
    return chr(random.randint(65, 90))


def rand_lower():
    return chr(random.randint(97, 122))


def verify_code(n=4):
    ls = []
    for i in range(n):
        choose = random.randint(1, 3)
        if choose == 1:
            s = rand_num()
        elif choose == 2:
            s = rand_upper()
        elif choose == 3:
            s = rand_lower()
        ls.append(s)
    return "".join(ls)


print(verify_code())