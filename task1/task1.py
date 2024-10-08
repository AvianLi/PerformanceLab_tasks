from collections import deque

def circular_array_path(n, m):
    dq = deque(range(1, n + 1))  # Создаем двустороннюю очередь от 1 до n
    result = [dq[0]]  
    dq.rotate(-(m % n))  # Сдвигаем очередь, учитывая отрицательные значения m

    while dq[0] != result[0]:  
        result.append(dq[0])  
        dq.rotate(-(m % n))  

    return ''.join(map(str, result))  

n = int(input("Введите длину массива (n): "))
m = int(input("Введите шаг (m): "))

result = circular_array_path(n, m)
print("Полученный путь:", result)
