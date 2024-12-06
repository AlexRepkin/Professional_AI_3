#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_words(matrix, words):
    rows, cols = len(matrix), len(matrix[0])
    word_set = set(words)
    found_words = set()
    # 8 направлений
    directions = [
        (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
    ]

    def dfs(x, y, visited, current_word):
        # Если текущее слово есть в словаре - в найденные
        if current_word in word_set:
            found_words.add(current_word)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                dfs(nx, ny, visited | {(nx, ny)}, current_word + matrix[nx][ny])

    # Запуск DFS с каждой клетки
    for i in range(rows):
        for j in range(cols):
            dfs(i, j, {(i, j)}, matrix[i][j])
    return found_words


if __name__ == "__main__":
    # Пример входных данных
    matrix = [
        ['М', 'С', 'Е'],
        ['Р', 'А', 'Т'],
        ['Л', 'О', 'Н']
    ]
    print("Исходная матрица:")
    for row in matrix:
        print(" ".join(row))
    words = ['МАРС', 'СОН', 'ЛЕТО', 'ТОН']
    print("Доступные слова:", words)
    # Поиск слов в матрице
    result = find_words(matrix, words)
    print("Найденные слова:", result)
