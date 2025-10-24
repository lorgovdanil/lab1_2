def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        if not swapped:
            break

    return numbers


def main():
    print()

    try:
        n = int(input("Введите количество чисел для сортировки: "))

        if n <= 0:
            print("Количество чисел должно быть положительным!")
            return

        numbers = []
        print(f"\nВведите {n} чисел:")

        for i in range(n):
            while True:
                try:
                    num = float(input(f"Число {i + 1}: "))
                    numbers.append(num)
                    break
                except ValueError:
                    print("Пожалуйста, введите корректное число!")

        print(f"\nИсходный список: {numbers}")

        sorted_numbers = bubble_sort(numbers.copy())

        print(f"Отсортированный список: {sorted_numbers}")

        print(f"\nМинимальное число: {sorted_numbers[0]}")
        print(f"Максимальное число: {sorted_numbers[-1]}")

    except ValueError:
        print("Ошибка: пожалуйста, введите корректное целое число для количества!")
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()