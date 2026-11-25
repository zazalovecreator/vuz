##1
'''
class Student:
    course = "Data Science"


s1 = Student()
s1.name = "Иван"
s1.surname = "Иванов"
s1.semester = 1

result = s1.__dict__
print(result)
'''


##2
'''
class Group:
    members = []


class Student:
    course = "Data Science"


s1 = Student()
s1.name = 'Иван'
s1.surname = 'Иванов'
s1.semester = 1

s2 = Student()
s2.name = 'Лев'

print(s1.__dict__)
print(s2.__dict__)
'''


##3
'''
class User:
    def set_private_key(self, key):
        self.private_key = key

    def show_private_key(self):
        print(f'Приватный ключ пользователя {self.private_key}')
'''


##4
'''
class PasswordChecker:
    def set_password_range(self, min_len, max_len):
        self.min_len = min_len
        self.max_len = max_len

    def check_passwords(self, passwords):
        return [self.min_len <= len(p) <= self.max_len for p in passwords]
'''


##5
'''
class Book:
    genre = "Programming"


b1 = Book()
b1.title = "Python for Beginners"
b1.author = "John Doe"
b1.pages = 350

result = b1.__dict__
print(result)
'''


##6
'''
class Employee:
    department = "IT"


emp1 = Employee()
emp1.first_name = "Anna"
emp1.last_name = "Smith"
emp1.experience = 5

result = emp1.__dict__
print(result)
'''


##7
'''
class Product:
    category = "Electronics"


p1 = Product()
p1.name = "Laptop"
p1.brand = "Dell"
p1.price = 1200

result = p1.__dict__
print(result)
'''


##8
class Department:
    teachers = []


class Teacher:
    pass


t1 = Teacher()
t1.name = 'Мария'
t1.surname = 'Петрова'
t1.subject = 'Математика'

t2 = Teacher()
t2.name = 'Алексей'
t2.surname = 'Сидоров'
t2.subject = 'Физика'

print(t1.__dict__)
print(t2.__dict__)
