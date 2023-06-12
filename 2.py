grade_list = [1, 3, 2, 2, 2, 3, 3, 4, 5, 5]

for i in range(len(grade_list)):
    if grade_list[i] == 4:
        grade_list[i] = 2
    elif grade_list[i] == 5:
        grade_list[i] = 1

print(grade_list)