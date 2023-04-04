def open_file(file_name):
    file = open(file_name, "r", encoding="UTF-8")
    id_name_dict = dict()
    id_grade_dict = dict()
    for line in file:
        line = line.strip()
        row = line.split(",")
        id_name_dict.update({row[0]: row[1]})
        id_grade_dict.update({row[0]: row[2]})
    file.close()
    return id_name_dict, id_grade_dict


def avg_grade(id_grade_dict):
    count = 0
    avg = 0
    for key in id_grade_dict:
        avg = avg + int(id_grade_dict[key])
        count += 1
    return avg / count


def max_grade(id_grade_dict):
    max_score = 0
    for key in id_grade_dict:
        if max_score <= int(id_grade_dict[key]):
            max_score = int(id_grade_dict[key])
    return max_score


def min_grade(id_grade_dict):
    min_score = 100
    for key in id_grade_dict:
        if min_score >= int(id_grade_dict[key]):
            min_score = int(id_grade_dict[key])
    return min_score


def get_id(id_grade_dict, grade):
    ids = list(id_grade_dict.keys())
    grades = list(id_grade_dict.values())
    id_list = []
    grade_index_list = []
    i = 0
    while grade in grades:
        grade_index_list.append(grades.index(grade) + i)
        grades.remove(grade)
        i = i+1
    for item in grade_index_list:
        id_list.append(ids[item])
    return id_list


max_name_list = ''
min_name_list = ''

name_dict, grade_dict = open_file("./013.读取成绩文件计算平均分、最高最低分.txt")
avg_score = avg_grade(grade_dict)
max_score = max_grade(grade_dict)
min_score = min_grade(grade_dict)
max_id_list = get_id(grade_dict, str(max_score))
min_id_list = get_id(grade_dict, str(min_score))
for item in max_id_list:
    max_name_list = max_name_list + name_dict[item] + '、'
for item in min_id_list:
    min_name_list = min_name_list + name_dict[item] + '、'
print(f"平均分为：{avg_score},\n最高分为：{max_score},由{max_name_list.strip('、')}获得\n最低分为：{min_score},由{min_name_list.strip('、')}获得。")
