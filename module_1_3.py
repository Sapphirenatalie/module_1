# Создайте переменные разных типов данных:
# Создайте переменную name и присвойте ей значение вашего имени (строка).
# Выведите значение переменной name на экран.
# Создайте переменную age и присвойте ей значение вашего возраста (целое число).
# Выведите значение переменной age на экран.
# Перезапишите в age текущее значение переменной age + новое.
# Как неверно (просто перезапись на новое число):
# a = 15
# a = 17
# Выведите измененное значение переменной age на экран.
# Создайте переменную is_student и присвойте ей значение True (логическое значение).
# Выведите значение переменной is_student на экран.
# Пример результата выполнения программы:
# Name: John
# Age: 25
# New Age: 26
# Is Student: True

name = "Natalia"  # first version
print(name)
age = 56
print(age)
new_age = age + 1
print(new_age)
is_student = True
print(is_student)

print("--------")
title_name = 'Name: '  # second version
name = "Natalia"
print(title_name + name)
title_age = 'Age: '
age = 56
print(title_age, age)
new_age_title = 'New age: '
new_age = age + 1
print(new_age_title + str(new_age))
student_title = 'Is Student: '
is_student = True
print(student_title + str(is_student))
