import random  # модуль для генерации случайных чисел

DIGITS = 4  # длина загаданного числа


def make_secret():
    # Загадывает число из 4 разных цифр (первая цифра не 0)
    first = random.choice("123456789")
    # остальные цифры выбираются без повторов и не совпадают с первой
    rest = random.sample([d for d in "0123456789" if d != first], DIGITS - 1)
    return first + "".join(rest)


def count_bulls_cows(secret, guess):
    # Быки: совпадение цифры и позиции
    bulls = sum(s == g for s, g in zip(secret, guess))
    # Коровы: общие цифры минус быки
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows


def is_valid(guess):
    # Проверка: 4 символа, только цифры, все цифры разные
    return len(guess) == DIGITS and guess.isdigit() and len(set(guess)) == DIGITS


def play():
    secret = make_secret()  # загадываем число
    moves = 0               # счётчик ходов
    print(f"Я загадал {DIGITS}-значное число с разными цифрами. Угадай!")
    print("(введи 'q', чтобы сдаться)")

    while True:
        guess = input("Твоя догадка: ").strip()
        if guess.lower() in ("q", "й"):  # игрок сдался
            print(f"Загаданное число было: {secret}")
            return
        if not is_valid(guess):  # некорректный ввод не считается ходом
            print(f"Нужно {DIGITS} разные цифры, например 1234.")
            continue

        moves += 1
        bulls, cows = count_bulls_cows(secret, guess)
        print(f"Быков: {bulls}, Коров: {cows}")

        if bulls == DIGITS:  # все цифры на своих местах — победа
            print(f"Победа! Ты угадал число {secret} за {moves} ходов.")
            return


def main():
    print("=== Быки и коровы ===")
    print("Бык — угадана цифра и её точная позиция.")
    print("Корова — цифра есть в загаданном числе, но стоит на другом месте.")
    while True:
        answer = input("Чтобы играть, введи 'у' (любой другой ввод — выход): ").strip().lower()
        # принимаем и русскую 'у', и английскую 'y'
        if answer in ("у", "y"):
            play()
        else:
            print("Пока!")
            break


if __name__ == "__main__":
    main()
