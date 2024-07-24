# Неизменяемые и изменяемые объекты. Кортежи и списки
# Задайте переменные разных типов данных:
# Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
# Выполните операции вывода кортежа immutable_var на экран.
# Изменение значений переменных:
# Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
# Создание изменяемых структур данных:
# Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
# Измените элементы списка mutable_list.
# Выведите на экран измененный список mutable_list.
# Пример результата выполнения программы:
# Immutable tuple: (1, 2, 'a', 'b')
# Mutable list: [1, 2, 'a', 'b', 'Modified']

immutable_var = (2023, 2024, 'abc', False)
print('Immutable tuple: ', immutable_var)

# immutable_var[0][0]=2020 # неизменяемый тип
# изменить можно лишь элемент списка, который находится внутри кортежа
# (immutable_var)=([20, 21, 22], 23)
# immutable_var[0][0]=19
# print(immutable_var)

mutable_list = [1, 2, 3, 'letter', True]
print('Mutable list: ', mutable_list)
mutable_list.append(20)
print(mutable_list)
mutable_list.extend([False])
print(mutable_list)
mutable_list[1] = 'Fruits'
mutable_list[-1] = 'Modified'
print(mutable_list)
