
class STUDENT:
    def __init__(self, fio, numb, grade):
        self.fio = fio
        self.numb = numb
        self.grade = grade

def main():
    n = int(input(f'Сколько студентов? Введи число:'))
    students = []
    for i in range(n):
        print('')
        fio = input("Введи фамилию и инициалы:")
        numb = input("Введи номер группы:")
        grade = list(map(int, input("Введи 5 оценок студента через пробел:").split()))
        students.append(STUDENT(fio, numb, grade))
    students.sort(key=lambda x: x.fio)

    failing_students = []

    for i in students:
        if 2 in i.grade:
            failing_students.append(i)

    while True:
        print('---------------------------------------------')
        print('1 - все студенты, 2 - с двойками')
        if int(input('Ввод:')) == 1:
            for student in students:
                print(student.fio, student.numb, student.grade)
        else:
            if len(failing_students) == 0:
                print('Все студенты молодцы! Учатся без двоек')
            else:
                for student in failing_students:
                    print(student.fio, student.numb, student.grade)

main()