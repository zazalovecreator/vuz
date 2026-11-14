class LetterNode:
    def __init__(self, letter=None):
        self.letter = letter
        self.next_letter = None


class LinkedList:
    def __init__(self):
        self.head = None

    def AddToEnd(self, new_letter):
        new_letter_node = LetterNode(new_letter)
        if self.head is None:
            self.head = new_letter_node
            return
        last_letter_node = self.head
        while last_letter_node.next_letter is not None:
            last_letter_node = last_letter_node.next_letter
        last_letter_node.next_letter = new_letter_node

    def AddToBeginning(self, new_letter):
        new_letter_node = LetterNode(new_letter)
        new_letter_node.next_letter = self.head
        self.head = new_letter_node

    def AddToPosition(self, letter_to_add, position):
        if position < 0:
            print("Такой позиции нет в списке")
            return
        if position == 0:
            self.AddToBeginning(letter_to_add)
            return
        last_letter_node = self.head
        letter_node_index = 0
        while last_letter_node is not None and letter_node_index < position - 1:
            last_letter_node = last_letter_node.next_letter
            letter_node_index += 1
        if last_letter_node is None:
            print("Такой позиции нет в списке")
            return
        new_letter_node = LetterNode(letter_to_add)
        new_letter_node.next_letter = last_letter_node.next_letter
        last_letter_node.next_letter = new_letter_node

    def RemByMean(self, meaning):
        if self.head is None:
            print("Список пуст")
            return
        if self.head.letter == meaning:
            self.head = self.head.next_letter
            return
        last_letter_node = self.head
        while last_letter_node.next_letter is not None:
            if last_letter_node.next_letter.letter == meaning:
                last_letter_node.next_letter = last_letter_node.next_letter.next_letter
                return
            last_letter_node = last_letter_node.next_letter
        print("Элемент не найден")

    def RemByNumb(self, numb):
        if self.head is None or numb < 0:
            print("Неправильная позиция")
            return
        if numb == 0:
            self.head = self.head.next_letter
            return
        last_letter_node = self.head
        letter_node_index = 0
        while last_letter_node is not None and letter_node_index < numb - 1:
            last_letter_node = last_letter_node.next_letter
            letter_node_index += 1
        if last_letter_node is None or last_letter_node.next_letter is None:
            print("Неправильная позиция")
            return
        last_letter_node.next_letter = last_letter_node.next_letter.next_letter

    def Clear(self):
        head_letter = self.head
        while head_letter is not None:
            next_letter_node = head_letter.next_letter
            head_letter.next_letter = None
            head_letter = next_letter_node
        self.head = None
        print("Список очищен")

    def FindNumbByMean(self, meaning):
        letter_node_index = 0
        head_letter = self.head
        while head_letter is not None:
            if head_letter.letter == meaning:
                return letter_node_index
            head_letter = head_letter.next_letter
            letter_node_index += 1
        return -1

    def Look(self):
        if self.head is None:
            print("Список пуст")
            return
        letters = []
        head_letter = self.head
        while head_letter is not None:
            letters.append(head_letter.letter)
            head_letter = head_letter.next_letter
        print(" -> ".join(letters))

    def Fill(self, sentence):
        for symbol in sentence:
            if symbol == ".":
                break
            if symbol.isalpha():
                self.AddToEnd(symbol)


def ReadInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Нужно ввести целое число")


def ReadLetter(prompt):
    while True:
        letter = input(prompt)
        if len(letter) == 1 and letter.isalpha():
            return letter
        print("Нужно ввести одну букву")


def main():
    letters = LinkedList()
    sentence = input("Введите предложение, оканчивающееся точкой: ")
    while not sentence.endswith("."):
        sentence = input("Предложение должно оканчиваться точкой: ")
    letters.Fill(sentence)
    print("Список построен:")
    letters.Look()

    while True:
        print("\n1. Добавить в конец")
        print("2. Добавить в начало")
        print("3. Добавить в позицию")
        print("4. Удалить по значению")
        print("5. Удалить по номеру")
        print("6. Очистить список")
        print("7. Найти номер элемента")
        print("8. Просмотр списка")
        print("0. Выход")
        choice = input("Выберите пункт: ")

        match choice:
            case "1":
                letters.AddToEnd(ReadLetter("Буква: "))
            case "2":
                letters.AddToBeginning(ReadLetter("Буква: "))
            case "3":
                letter = ReadLetter("Буква: ")
                position = ReadInt("Позиция (с 0): ")
                letters.AddToPosition(letter, position)
            case "4":
                letters.RemByMean(ReadLetter("Буква для удаления: "))
            case "5":
                letters.RemByNumb(ReadInt("Номер (с 0): "))
            case "6":
                letters.Clear()
            case "7":
                index = letters.FindNumbByMean(ReadLetter("Буква для поиска: "))
                if index == -1:
                    print("Элемент не найден")
                else:
                    print(f"Номер элемента: {index}")
            case "8":
                letters.Look()
            case "0":
                break
            case _:
                print("Нет такого пункта")


if __name__ == "__main__":
    main()