#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random
import string


def longest_path(matrix, first_letter):
    rows, cols = len(matrix), len(matrix[0])

    def dfs(x, y, previous_char, met_chars):
        # Если клетка вне матрицы или символ не по алфавиту
        if not (0 <= x < rows and 0 <= y < cols) or matrix[x][y] != previous_char:
            return 0, []
        # Если клетка посещённая
        if (x, y) in met_chars:
            return met_chars[(x, y)]
        max_length = 0
        # Куда можно двигаться, все 8 сторон
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        max_path = []
        # Рекурсивный поиск пути в каждом направлении
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            length, path = dfs(nx, ny, chr(ord(previous_char) + 1), met_chars)
            if length > max_length:
                max_length = length
                max_path = path
        # Сохранение результата с учётом текущей клетки и пути
        met_chars[(x, y)] = (1 + max_length, [(x, y)] + max_path)
        return met_chars[(x, y)]

    max_length = 0
    max_path = []
    # Нахождение всех нужных символов, с которых начинается поиск
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == first_letter:
                length, path = dfs(i, j, first_letter, {})
                if length > max_length:
                    max_length = length
                    max_path = path
    return max_length, max_path


def print_with_path(matrix, path):
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if (i, j) in path:
                print(f"\033[91m{char}\033[0m", end=" ")
            else:
                print(char, end=" ")
        print()


# Основная программа
if __name__ == "__main__":
    # Пример матрицы
    matrix = [
        ['D', 'E', 'H', 'X', 'B'],
        ['A', 'O', 'G', 'P', 'E'],
        ['D', 'D', 'C', 'F', 'D'],
        ['E', 'B', 'E', 'A', 'S'],
        ['C', 'D', 'Y', 'E', 'N']
    ]
    print("Исходная матрица:")
    for row in matrix:
        print(" ".join(row))
    # Пользовательский ввод символа
    first_letter = input("Начальный символ? - ").strip().upper()
    if len(first_letter) != 1 or not first_letter.isalpha():
        raise ValueError("Нужна лишь 1 буква.")
    else:
        # Поиск максимального пути
        max_length, path = longest_path(matrix, first_letter)
        print("Длина самого длинного пути =", max_length)
        print("Матрица с выделенным путём:")
        print_with_path(matrix, path)

    # Генерация случайной матрицы
    print("\nСлучайная матрица:")
    columns = random.randint(4, 10)
    random_matrix = [[random.choice(string.ascii_uppercase)
                      for _ in range(columns)] for _ in range(random.randint(4, 10))]
    for row in random_matrix:
        print(" ".join(row))
    random_first_letter = input(
        "Введите начальный символ для случайной матрицы: ").strip().upper()
    if len(random_first_letter) != 1 or not random_first_letter.isalpha():
        print("Ошибка: Введите один буквенный символ.")
    else:
        max_length, path = longest_path(random_matrix, random_first_letter)
        print(f"Длина самого длинного пути =", max_length)
        print("Матрица с выделенным путём:")
        print_with_path(random_matrix, path)
