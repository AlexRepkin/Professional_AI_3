#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random


# Словарь цветов для букв
colors = {
    " ": "\033[40m",  # Черный фон
    "R": "\033[41m",  # Красный фон
    "G": "\033[42m",  # Зеленый фон
    "Y": "\033[43m",  # Желтый фон
    "X": "\033[44m",  # Синий фон
    "B": "\033[45m",  # Фиолетовый фон
    "C": "\033[46m",  # Бирюзовый фон
    "W": "\033[47m",  # Белый фон
}


def generate_random_matrix(rows, cols, keys=None):
    # Генерирует матрицу случайных символов на основе переданных ключей
    if keys is None:
        keys = list(colors.keys())
    return [[random.choice(keys) for _ in range(cols)] for _ in range(rows)]


def print_matrix(matrix):
    for row in matrix:
        for cell in row:
            color = colors.get(cell, "\033[40m")  # Черный фон по умолчанию
            print(f"{color}  \033[0m", end="")  # Печать цветного квадрата
        print()  # Переход на новую строку
    print("\033[0m")  # Сброс цвета


def flood_fill(matrix, start_node, target_color, replacement_color):
    rows, cols = len(matrix), len(matrix[0])
    x, y = start_node

    # Если начальный узел уже имеет цвет замены или цвет не совпадает с целевым
    if matrix[x][y] != target_color or target_color == replacement_color:
        return matrix

    # Функция поиска в глубину
    def dfs(r, c):
        # Если координаты выходят за границы или цвет не совпадает с целевым
        if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] != target_color:
            return

        # Заменяем цвет
        matrix[r][c] = replacement_color

        # Рекурсивно проверяем соседей
        dfs(r + 1, c)  # вниз
        dfs(r - 1, c)  # вверх
        dfs(r, c + 1)  # вправо
        dfs(r, c - 1)  # влево

    # Запускаем DFS с начального узла
    dfs(x, y)
    return matrix


if __name__ == '__main__':
    matrix = [
        ["Y", "Y", "Y", "G", "G", "G", "G", "G", "G", "G"],
        ["Y", "Y", "Y", "Y", "Y", "Y", "G", "X", "X", "X"],
        ["G", "G", "G", "G", "G", "G", "G", "X", "X", "X"],
        ["W", "W", "W", "W", "W", "G", "G", "G", "G", "X"],
        ["W", "R", "R", "R", "R", "R", "G", "X", "X", "X"],
        ["W", "W", "W", "R", "R", "G", "G", "X", "X", "X"],
        ["W", "B", "W", "R", "R", "R", "R", "R", "R", "X"],
        ["W", "B", "B", "B", "B", "R", "R", "X", "X", "X"],
        ["W", "B", "B", "X", "B", "B", "B", "B", "X", "X"],
        ["W", "B", "B", "X", "X", "X", "X", "X", "X", "X"],
    ]
    start_node = (3, 9)
    target_color = "X"
    replacement_color = "C"
    print("Исходная матрица:")
    print_matrix(matrix)
    matrix = flood_fill(matrix, start_node, target_color, replacement_color)
    print("Матрица после заливки:")
    print_matrix(matrix)
    # Генерация случайной матрицы
    random_rows = random.randint(5, 15)
    random_columns = random.randint(5, 15)
    matrix = generate_random_matrix(random_rows, random_columns)
    # Выбор случайной начальной точки
    random_start_node = (random.randint(0, random_rows - 1), random.randint(0, random_columns - 1))
    random_target_color = matrix[random_start_node[0]][random_start_node[1]]  # Цвет в начальной точке
    random_replacement_color = random.choice([c for c in colors.keys() if c != random_target_color])  # Цвет замены
    print("Сгенерированная матрица:")
    print_matrix(matrix)
    print(f"Начальная точка: {random_start_node}, целевой цвет:"
          f"{random_target_color}, цвет замены: {random_replacement_color}")
    # Выполнение заливки
    matrix = flood_fill(matrix, random_start_node, random_target_color, random_replacement_color)
    print("Матрица после заливки:")
    print_matrix(matrix)
