from collections import deque

def circular_array_path(n, m):
    dq = deque(range(1, n + 1))  # Создаем двустороннюю очередь от 1 до n
    result = [dq[0]]  # Начинаем с первого элемента
    dq.rotate(-(m - 1))  # Сдвигаем очередь на (m-1) шагов

    while dq[0] != result[0]:  # Пока не вернемся к первому элементу
        result.append(dq[0])  # Добавляем элемент в результат
        dq.rotate(-(m - 1))  # Снова сдвигаем очередь

    return ''.join(map(str, result))  # Возвращаем путь в виде строки

# Ввод данных через консоль
n = int(input("Введите длину массива (n): "))
m = int(input("Введите шаг (m): "))

# Вывод результата
result = circular_array_path(n, m)
print("Полученный путь:", result)