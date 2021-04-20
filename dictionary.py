students = [{"name": "Vova",
             "last_name": "Zinkovsky",
             "age": 17,
             "scores": [1, 2, 3, 4, 5],
             "hobbies": ['play', 'programming', 'reading']
             },
            {"name": "Begimai",
             "last_name": "Zhumakova",
             "age": 18,
             "scores": [5, 5, 3, 4, 5],
             "hobbies": ['pubg', 'programming', 'reading', 'walking']
             },
            {"name": "Aliya",
             "last_name": "Andabekova",
             "age": 18,
             "scores": [1, 4, 3, 1, 2],
             "hobbies": ['programming', 'reading', 'drawing']
             },
            {"name": "Cholpon",
             "last_name": "Kaimova",
             "age": 16,
             "scores": [5, 2, 4, 4, 5],
             "hobbies": ['pubg', 'programming', 'reading', 'anime', ]
             },
            {"name": "Bakyt",
             "last_name": "Asanaliev",
             "age": 35,
             "scores": [4, 2, 4, 4, 5],
             "hobbies": ['play', 'programming', 'reading', 'footbal', 'history']
             },
            {"name": "Maksim",
             "last_name": "Surovkin",
             "age": 22,
             "scores": [],
             "hobbies": ['programming', 'reading', 'traveling', 'cycling']
             }
            ]
general_avg = 0
student_avg = []
std = 0
for student in students:
    sum = 0
    for score in student['scores']:
        sum += score
        try:
            students_avg = sum / len(student['scores'])
        except ZeroDivisionError:
            students_avg = 0
    student_avg.append(students_avg)
sum_avg = 0
for avg in student_avg:
    sum_avg += avg
    general_avg = sum_avg / len(student_avg)
max = 0
min = 5
i = 0

while i < len(student_avg):
    if student_avg[i] > max:
        max = student_avg[i]
    elif student_avg[i] < min:
        min = student_avg[i]
    i += 1
std = max - min
print("student average:", student_avg)
print("general average:", round(general_avg, 2))
print("std:", round(std, 2))

dict_loop = 0

import pprint

for student in students:
    student['avg'] = student_avg[dict_loop]
    dict_loop += 1
pprint.pprint(students)
