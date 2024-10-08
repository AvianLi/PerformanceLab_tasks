import sys

# Функция для получения данных о круге из файла
def get_circle_data(file_name):
    # Открываем файл и читаем данные
    with open(file_name, 'r') as f:
        x, y = map(float, f.readline().split())
        r = float(f.readline())
    return (x, y, r)

# Функция для получения данных о точках из файла
def get_points_data(file_name):
    points = []
    with open(file_name, 'r') as f:
        for line in f:
            points.append(tuple(map(float, line.split())))
    return points

# Функция для определения положения точки относительно окружности
def point_position(circle, point):
    x_center, y_center, radius = circle
    x_point, y_point = point
    distance_squared = (x_point - x_center) ** 2 + (y_point - y_center) ** 2
    radius_squared = radius ** 2

    if distance_squared == radius_squared:
        return 0  # Точка на окружности
    elif distance_squared < radius_squared:
        return 1  # Точка внутри окружности
    else:
        return 2  # Точка вне окружности

# Основная функция программы
def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <circle.txt> <points.txt>")
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    # Читаем данные окружности и точек
    circle = get_circle_data(circle_file)
    points = get_points_data(points_file)

    # Для каждой точки вычисляем её положение относительно окружности
    for point in points:
        print(point_position(circle, point))

# Запуск основной функции, если скрипт запускается напрямую
if __name__ == "__main__":
    main()
