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

TURNS = 4        # сколько витков
POINTS = 400     # сколько точек в спирали (больше - глаже)
RADIUS = 1.0     # радиус спирали
HEIGHT = 10.0    # высота
SPEED = 0.05     # скорость вращения

z = np.linspace(0, HEIGHT, POINTS)
phase = z / HEIGHT * TURNS * 2 * np.pi

fig = plt.figure(figsize=(6, 8))
ax = fig.add_subplot(projection="3d")
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(0, HEIGHT)
ax.set_box_aspect((1, 1, 3))
ax.axis("off")

line1, = ax.plot([], [], [], lw=3, color="tab:blue")
line2, = ax.plot([], [], [], lw=3, color="tab:red")


def update(frame):
    a = phase + frame * SPEED
    line1.set_data_3d(RADIUS * np.cos(a), RADIUS * np.sin(a), z)
    line2.set_data_3d(RADIUS * np.cos(a + np.pi), RADIUS * np.sin(a + np.pi), z)
    return line1, line2


anim = FuncAnimation(fig, update, interval=20, cache_frame_data=False)
plt.show()
