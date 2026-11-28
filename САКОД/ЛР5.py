import string


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def AddToEnd(self, value):
        node = Node(value)
        node.prev = self.tail
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

    def AddToBeginning(self, value):
        node = Node(value)
        node.next = self.head
        if self.head is None:
            self.tail = node
        else:
            self.head.prev = node
        self.head = node
        self.size += 1

    def RemoveNode(self, node):
        if node is None:
            return
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        self.size -= 1

    def RemByMean(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                self.RemoveNode(node)
                return True
            node = node.next
        return False

    def Clear(self):
        while self.head is not None:
            self.RemoveNode(self.head)

    def FindNumbByMean(self, value):
        node = self.head
        number = 0
        while node is not None:
            if node.value == value:
                return number
            node = node.next
            number += 1
        return -1

    def Look(self):
        node = self.head
        values = []
        while node is not None:
            values.append(str(node.value))
            node = node.next
        print(' <-> '.join(values) if values else 'Список пуст')

    def MeanOfMin(self):
        if self.size < 4 or self.size % 2 != 0:
            raise ValueError('Нужно чётное количество чисел (не менее 4)')
        left = self.head
        right = self.tail
        total = 0
        n = self.size // 2
        for _ in range(n):
            total += min(left.value, right.value)
            left = left.next
            right = right.prev
        return total / n


def ReadFloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Введите действительное число')


def ReadChar(prompt):
    while True:
        value = input(prompt)
        if len(value) == 1:
            return value
        print('Введите один символ')


def Menu(items, read):
    while True:
        print('\n1. Добавить в конец\n2. Добавить в начало')
        print('3. Удалить по значению\n4. Очистить список')
        print('5. Найти номер элемента\n6. Просмотр списка\n0. Выход')
        choice = input('Выберите пункт: ')
        if choice == '1':
            items.AddToEnd(read('Элемент: '))
        elif choice == '2':
            items.AddToBeginning(read('Элемент: '))
        elif choice == '3':
            if not items.RemByMean(read('Элемент: ')):
                print('Элемент не найден')
        elif choice == '4':
            items.Clear()
        elif choice == '5':
            number = items.FindNumbByMean(read('Элемент: '))
            print('Номер (с 0):', number) if number != -1 else print('Элемент не найден')
        elif choice == '6':
            items.Look()
        elif choice == '0':
            break
        else:
            print('Нет такого пункта')


def main():
    numbers = LinkedList()
    while True:
        try:
            n = int(input('Введите n (n >= 2): '))
            if n >= 2:
                break
        except ValueError:
            pass
        print('Введите целое число не меньше 2')
    for i in range(2 * n):
        numbers.AddToEnd(ReadFloat(f'a{i + 1}: '))
    numbers.Look()
    print('Среднее минимумов:', numbers.MeanOfMin())
    Menu(numbers, ReadFloat)

    letters = LinkedList()
    punctuation = string.punctuation + '«»—…–“”„’'
    while True:
        symbol = ReadChar('Введите символ (точка — конец): ')
        if symbol == '.':
            break
        if symbol in punctuation:
            letters.RemoveNode(letters.tail)
        else:
            letters.AddToEnd(symbol)
    letters.Look()
    Menu(letters, ReadChar)


if __name__ == '__main__':
    main()
