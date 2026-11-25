##1
'''
def rectangle_area(a, b):
    return a * b


for i in range(1, 4):
    a = float(input(f'Прямоугольник {i}. Введите сторону a: '))
    b = float(input(f'Прямоугольник {i}. Введите сторону b: '))
    print(f'Площадь прямоугольника {i} = {rectangle_area(a, b)}')
'''


##2
'''
import math


def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


areas = []
for i in range(1, 4):
    a = float(input(f'Треугольник {i}. Сторона a: '))
    b = float(input(f'Треугольник {i}. Сторона b: '))
    c = float(input(f'Треугольник {i}. Сторона c: '))
    s = triangle_area(a, b, c)
    areas.append(s)
    print(f'Площадь треугольника {i} = {s:.2f}')

if areas[0] == areas[1] == areas[2]:
    print('Треугольники равновеликие')
else:
    print('Треугольники не являются равновеликими')
'''


##3
'''
import math


def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)


a1 = float(input('Первый треугольник. Катет a: '))
b1 = float(input('Первый треугольник. Катет b: '))
a2 = float(input('Второй треугольник. Катет a: '))
b2 = float(input('Второй треугольник. Катет b: '))

h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)

print(f'Гипотенуза первого треугольника = {h1:.2f}')
print(f'Гипотенуза второго треугольника = {h2:.2f}')

if h1 > h2:
    print('Гипотенуза первого треугольника больше')
elif h1 < h2:
    print('Гипотенуза второго треугольника больше')
else:
    print('Гипотенузы равны')
'''


##4
'''
def array_stats(arr):
    total = sum(arr)
    average = total / len(arr)
    return total, average


arrays = [
    [4, 8, 15, 16, 23, 42],
    [10, 20, 30, 40],
    [1, 2, 3, 4, 5, 6, 7],
]

for i, arr in enumerate(arrays, 1):
    total, average = array_stats(arr)
    print(f'Массив {i}: {arr}')
    print(f'  Сумма = {total}, среднее арифметическое = {average:.2f}')
'''


##5
'''
import math


def circle_area(r):
    return math.pi * r ** 2


def rectangle_area(a, b):
    return a * b


def triangle_area(base, height):
    return 0.5 * base * height


print('Выберите фигуру: 1 - круг, 2 - прямоугольник, 3 - треугольник')
choice = int(input('Ваш выбор: '))

if choice == 1:
    r = float(input('Введите радиус: '))
    print(f'Площадь круга = {circle_area(r):.2f}')
elif choice == 2:
    a = float(input('Введите сторону a: '))
    b = float(input('Введите сторону b: '))
    print(f'Площадь прямоугольника = {rectangle_area(a, b):.2f}')
elif choice == 3:
    base = float(input('Введите основание: '))
    height = float(input('Введите высоту: '))
    print(f'Площадь треугольника = {triangle_area(base, height):.2f}')
else:
    print('Неверный выбор')
'''


##6
'''
import math


def equilateral_triangle_area(side):
    return (math.sqrt(3) / 4) * side ** 2


def hexagon_area(a):
    # правильный шестиугольник состоит из 6 равносторонних треугольников
    return 6 * equilateral_triangle_area(a)


a = float(input('Введите сторону шестиугольника: '))
print(f'Площадь правильного шестиугольника = {hexagon_area(a):.2f}')
'''


##7
'''
import math


def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def quadrilateral_area(a, b, c, d, diagonal):
    # диагональ делит четырёхугольник на два треугольника
    s1 = triangle_area(a, b, diagonal)
    s2 = triangle_area(c, d, diagonal)
    return s1 + s2


a = float(input('Сторона a: '))
b = float(input('Сторона b: '))
c = float(input('Сторона c: '))
d = float(input('Сторона d: '))
diagonal = float(input('Диагональ: '))

print(f'Площадь четырёхугольника = {quadrilateral_area(a, b, c, d, diagonal):.2f}')
'''


##8
def square_perimeter(a):
    return 4 * a


def square_area(a):
    return a * a


for i in range(1, 4):
    a = float(input(f'Квадрат {i}. Введите сторону: '))
    print(f'Квадрат {i}: периметр = {square_perimeter(a)}, площадь = {square_area(a)}')
