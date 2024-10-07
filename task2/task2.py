# Функция для получения данных о круге из файла
def get_circle_data():
    # Открываем файл circle.txt
    with open('circle.txt', 'r') as f:
        # Чтение первой строки - координаты центра окружности (x, y)
        x, y = map(float, f.readline().split())
        # Чтение второй строки - радиус окружности
        r = float(f.readline())
    return (x, y, r)

# Функция для получения данных о точках из файла
def get_points_data():
    points = []
    # Открываем файл points.txt
    with open('points.txt', 'r') as f:
        # Чтение каждой строки, каждая строка содержит координаты одной точки (x, y)
        for line in f:
            points.append(tuple(map(float, line.split())))
    return points

# Функция для определения положения точки относительно окружности
def point_position(circle, point):
    x_center, y_center, radius = circle  # Координаты центра окружности и радиус
    x_point, y_point = point  # Координаты точки
    # Вычисление квадрата расстояния от точки до центра окружности
    distance_squared = (x_point - x_center) ** 2 + (y_point - y_center) ** 2
    # Квадрат радиуса окружности
    radius_squared = radius ** 2

    # Сравнение квадрата расстояния с квадратом радиуса
    if distance_squared == radius_squared:
        return 0  # Точка лежит на окружности
    elif distance_squared < radius_squared:
        return 1  # Точка внутри окружности
    else:
        return 2  # Точка снаружи окружности

# Основная функция программы
def main():
    # Читаем данные окружности и точек
    circle = get_circle_data()
    points = get_points_data()

    # Для каждой точки вычисляем её положение относительно окружности и выводим результат
    for point in points:
        print(point_position(circle, point))

# Запуск основной функции, если скрипт запускается напрямую
if __name__ == "__main__":
    main()