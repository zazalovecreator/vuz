##1
'''
class Project:
    tasks = []

class Project:
    def __init__(self, title, deadline, status):
        self.title = title
        self.deadline = deadline
        self.status = status
task1 = Project('Разработать макет', '2026-10-01', 'В работе')
task2 = Project('Написать тесты', '2026-10-15', 'Запланирована')
'''


##2
'''
class Team:
    players = []

class Player:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
p1 = Player('Игорь', 'Кузнецов', 'Нападающий')
p2 = Player('Дмитрий', 'Морозов', 'Защитник')
'''


##3
'''
class FileManager:
    def set_access_token(self, token):
        self.access_token = token
    def show_access_token(self):
        print(f"Токен доступа пользователя:{self.access_token}")
'''


##4
'''
class Auth:
    def set_secret_key(self, key):
        self.secret_key = key
    def show_secret_key(self):
        print(f"Секретный ключ аккаунта:{self.secret_key}")
'''


##5
'''
class Messenger:
    def set_user_id(self, key):
        self.user_id = key
    def show_user_id(self):
        print(f"Идентификатор пользователя:{self.user_id}")
'''


##6
'''
class EmailChecker:
    def set_required_chars(self, key):
        self.required = key
    def check_emails(self, emails):
        a = []
        for n in emails:
            a.append(all(x in n for x in self.required))
        print(a)
'''


##7
'''
class UsernameChecker:
    def set_allowed_symbols(self, spisok):
        self.allowed = spisok
    def check_usernames(self, uzernames):
        a = []
        for u in uzernames:
            a.append(all(x in self.allowed for x in u))
        print(a)
'''


##8
class CommentFilter:
    def set_forbidden_words(self, zapretki):
        self.forbidden = zapretki
    def check_comments(self, comments):
        a = []
        for c in comments:
            lower_c = c.lower()
            a.append(all(word not in lower_c for word in self.forbidden))
        return a
