def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

# Ввод последовательности чисел
sequence = input("Введите последовательность чисел через пробел: ")
numbers = [int(num) for num in sequence.split()]

# Ввод числа для поиска позиции
target = int(input("Введите число для поиска позиции: "))

# Сортировка списка с использованием слияния
sorted_numbers = merge_sort(numbers)

# Поиск позиции числа с использованием двоичного поиска
position = binary_search(sorted_numbers, target)

# Вывод результата
if position == len(sorted_numbers):
    print(f"Все числа в последовательности меньше введенного числа {target}.")
else:
    print(f"Номер позиции числа, которое меньше {target}, равен {position}.")


