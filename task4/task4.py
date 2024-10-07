import sys

# Функция для чтения чисел из файла
def read_numbers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [int(line.strip()) for line in file]
        return numbers
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        sys.exit(1)
    except ValueError:
        print("Ошибка: Неверный формат данных в файле.")
        sys.exit(1)

# Функция для подсчета минимальных шагов для приведения всех чисел к медиане
def min_moves_to_equal(nums):
    nums.sort()  # Сортируем числа
    median = nums[len(nums) // 2]  # Находим медиану
    # Считаем количество шагов для приведения всех чисел к медиане
    return sum(abs(num - median) for num in nums)

def main():
    # Читаем путь к файлу из аргументов командной строки
    file_path = sys.argv[1] if len(sys.argv) > 1 else input("Введите путь к файлу с числами: ")
    
    # Читаем числа из файла
    nums = read_numbers_from_file(file_path)
    
    # Вычисляем минимальное количество ходов для приведения всех чисел к одному
    moves = min_moves_to_equal(nums)
    
    # Выводим результат
    print(moves)

if __name__ == "__main__":
    main()
