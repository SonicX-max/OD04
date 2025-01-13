# Константная сложность O(1)
def get_first_element(arr):
    """
    Возвращает первый элемент массива.
    Сложность: O(1).
    """
    if arr:
        return arr[0]
    return None


# Линейная сложность O(n)
def sum_of_elements(arr):
    """
    Возвращает сумму всех элементов массива.
    Сложность: O(n).
    """
    total = 0
    for num in arr:
        total += num
    return total


# Логарифмическая сложность O(log n)
def binary_search(arr, target):
    """
    Бинарный поиск элемента в отсортированном массиве.
    Сложность: O(log n).
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    while True:
        print("\nВыберите алгоритм для тестирования:")
        print("1. Константная сложность (O(1))")
        print("2. Линейная сложность (O(n))")
        print("3. Логарифмическая сложность (O(log n))")
        print("0. Выход")

        choice = input("Введите номер алгоритма: ")
        if choice == "1":
            print("\n=== Константная сложность (O(1)) ===")
            user_input = input("Введите числа через запятую: ")
            arr = list(map(int, user_input.split(',')))
            print("Первый элемент массива:", get_first_element(arr))

        elif choice == "2":
            print("\n=== Линейная сложность (O(n)) ===")
            user_input = input("Введите числа через запятую: ")
            arr = list(map(int, user_input.split(',')))
            print("Сумма элементов массива:", sum_of_elements(arr))

        elif choice == "3":
            print("\n=== Логарифмическая сложность (O(log n)) ===")
            user_input = input("Введите числа через запятую (должны быть отсортированы): ")
            arr = list(map(int, user_input.split(',')))
            target = int(input("Введите число для поиска: "))
            result = binary_search(arr, target)
            if result != -1:
                print(f"Элемент {target} найден на индексе {result}.")
            else:
                print(f"Элемент {target} не найден.")

        elif choice == "0":
            print("Выход из программы. До свидания!")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")