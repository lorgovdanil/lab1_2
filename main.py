def bubble_sort(numbers, ascending=True):
    n = len(numbers)

    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):
            if ascending:
                condition = numbers[j] > numbers[j + 1]
            else:
                condition = numbers[j] < numbers[j + 1]

            if condition:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        if not swapped:
            break

    return numbers


def get_sorting_direction():
    print("\nВыберите направление сортировки:")
    print("1 - По возрастанию (от меньшего к большему)")
    print("2 - По убыванию (от большего к меньшему)")

    while True:
        choice = input("Ваш выбор (1 или 2): ").strip()

        if choice == "1":
            return True
        elif choice == "2":
            return False
        else:
            print("Неверный выбор! Пожалуйста, введите 1 или 2.")


def main():

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

        ascending = get_sorting_direction()

        sorted_numbers = bubble_sort(numbers.copy(), ascending)

        direction = "по возрастанию" if ascending else "по убыванию"
        print(f"\nСписок отсортированный {direction}: {sorted_numbers}")

        if ascending:
            print(f"Минимальное число: {sorted_numbers[0]}")
            print(f"Максимальное число: {sorted_numbers[-1]}")
        else:
            print(f"Максимальное число: {sorted_numbers[0]}")
            print(f"Минимальное число: {sorted_numbers[-1]}")

    except ValueError:
        print("Ошибка: пожалуйста, введите корректное целое число для количества!")
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()