# Задание "Средний балл":
# Вам необходимо решить задачу из реальной жизни:
# "школьные учителя устали подсчитывать вручную средний балл каждого ученика,
# поэтому вам предстоит автоматизировать этот процесс":

# На вход даны следующие данные:
# Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Например: 'Aaron' - [5, 3, 3, 5, 4]
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
# Напишите программу, которая составляет словарь, используя grades и students,
# где ключом будет имя ученика, а значением - его средний балл.

# Вывод в консоль:
# {'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}

# version 1
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

list1 = list(grades[0])
print('Grades of Aaron:', list1)
grade_1 = (sum(list1) / len(list1))
print('Average grade of Aaron:', grade_1)

list2 = list(grades[1])
print('Grades of Bilbo:', list2)
grade_2 = (sum(list2) / len(list2))
print('Average grade of Bilbo:', grade_2)

list3 = list(grades[2])
print('Grades of Johnny:', list3)
grade_3 = (sum(list3) / len(list3))
print('Average grade of Johnny:', grade_3)

list4 = list(grades[3])
print('Grades of Khendrik:', list4)
grade_4 = '%.2f' % (sum(list4) / len(list4))  # отображение числа с 2 знаками после запятой
print('Average grade of Khendrik:', grade_4)

list5 = list(grades[4])
print('Grades of Steve:', list5)
grade_5 = (sum(list5) / len(list5))
print('Average grade of Steve:', grade_5)

list_of_average_grades = [grade_1, grade_2, grade_3, grade_4, grade_5]
print('List of average grades:', list_of_average_grades)

list_of_students = list(students)
print('List of Students:', list_of_students)
list_of_students.sort()
list_of_students_abc = sorted(list_of_students)
print('List of students by alphabet:', list_of_students_abc)

grades_of_students = dict(zip(list_of_students_abc, list_of_average_grades))
print('Dictionary:', grades_of_students)

print('----------')
# version 2
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

average_grades = list([(sum(grades[0]) / len(grades[0])), (sum(grades[1]) / len(grades[1])),
                       (sum(grades[2]) / len(grades[2])), (sum(grades[3]) / len(grades[3])),
                       (sum(grades[4]) / len(grades[4]))])

students = list(sorted(students))

grades_of_students = dict(zip(students, average_grades))
print('Dictionary:', grades_of_students)
