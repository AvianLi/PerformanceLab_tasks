import json
import sys

# Функция для загрузки JSON-файла
def load_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Ошибка: Неверный формат JSON в файле '{file_path}'.")
        sys.exit(1)

# Рекурсивная функция для заполнения значений и удаления пустых 'values' и 'value'
def fill_values(tests, values_dict):
    for test in tests:
        # Заполняем поле value, если есть соответствие по id
        test_value = values_dict.get(test['id'], "")
        if test_value:
            test['value'] = test_value
        elif 'value' in test:
            del test['value']  # Удаляем пустое поле 'value'
        
        # Если есть вложенные значения (values), продолжаем рекурсию
        if 'values' in test:
            fill_values(test['values'], values_dict)
            
            # Удаляем поле 'values', если оно пустое после рекурсии
            if not test['values']:
                del test['values']

# Функция для создания итогового отчета
def create_report(tests, values, report_path):
    # Преобразуем список значений values.json в словарь для быстрого доступа
    values_dict = {value['id']: value['value'] for value in values}
    
    # Заполняем тесты значениями и удаляем пустые поля
    fill_values(tests['tests'], values_dict)
    
    # Записываем результат в report.json
    with open(report_path, 'w') as f:
        json.dump(tests, f, indent=4)

def main():
    # Проверяем количество аргументов командной строки
    if len(sys.argv) != 4:
        print("Usage: python script.py <values.json> <tests.json> <report.json>")
        sys.exit(1)

    # Получаем пути к файлам из аргументов командной строки
    values_file_path = sys.argv[1]
    tests_file_path = sys.argv[2]
    report_file_path = sys.argv[3]

    # Загружаем JSON-данные из файлов
    values_data = load_json(values_file_path)
    tests_data = load_json(tests_file_path)

    # Проверяем, что нужные данные есть в загруженных файлах
    if 'values' not in values_data or 'tests' not in tests_data:
        print("Ошибка: Неправильная структура файлов.")
        sys.exit(1)

    # Создаем отчет
    create_report(tests_data, values_data['values'], report_file_path)
    print(f"Отчет успешно создан в '{report_file_path}'.")

if __name__ == "__main__":
    main()
