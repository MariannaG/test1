#Практикум 1:

#  5 Как известно, кортеж является неизменяемым типом. Напишите программу, которая позволяет в кортеж A добавить кортеж B таким образом, что кортеж B помещается на index[2].
#      Пример: (1, 2, 3, 5, 8) (8,2,5) → (1, 2, 8, 2, 5, 3, 5, 8)
#   6 *Написать программу, которая для произвольного списка находит число / числа, наиболее часто встречающееся в данном списке и возвращающее их также в виде списка.

#      Примеры:
#    [1, 2, 3, 4, 7, 9, 9] → [9]
 #     [1, 2, 4, 6, 4, 6] → [4,6]

#  7 *Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.

#     Примеры:
#      1234565 seconds = 14:6:56:5
#--------------------------------------------------------------


#   1 Написать программу, запрашивающую имя, фамилию и возраст пользователя и выводящую строку вида:
#       Hello, <Фамилия пользователя> <Имя пользователя>. Your age is: <возраст>

#name = input("Enter your name please: ")
#surname = input("Enter your surname: ")
#age = input('Enter your age: ')
#print(f'Hello {name} {surname}. You age is {age}.')

#  2 Напишите программу, которая находит длину гипотенузы для прямоугольного треугольника по двум катетам. (с = sqrt(a * a  +  b * b))        0,5
#a = 152
#b = 1162
#c = (a ** 2 + b ** 2) ** 0.5
#print (c)



#  3 Пользователь вводит длины трех сторон треугольника (a,b,c) [тип float]. Напишите программу, которая проверяет, является ли треугольник прямоугольным (с2=a2+b2)

#a = float(input("Side A: "))
#b = float(input("Side B: "))
#c = float(input("Side C: "))

#print(c ** 2 == a ** 2 + b ** 2)

#  4 Пользователь вводит некоторый произвольный список list. Написать программу, выводящую элементы списка в обратном порядке. input
list = input("Enter something:")

list = str(list.reverse())
print(list)
