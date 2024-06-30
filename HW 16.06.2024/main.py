def main():
    scores = []
    for i in range(10):
        score = float(input(f"Введите оценку для студента {i+1}: "))
        while score < 1 or score > 12:
            print("Неверная оценка. Пожалуйста, введите оценку между 1 и 12.")
            score = float(input(f"Введите оценку для студента {i+1}: "))
        scores.append(score)

    while True:
        print("Меню:")
        print("1. Вывести оценки")
        print("2. Пересдача экзамена")
        print("3. Проверка стипендии")
        print("4. Сортировка оценок")
        print("5. Выход")
        choice = input("Введите ваш выбор (1-5): ")

        if choice == '1':
            print(scores)
        elif choice == '2':
            index = int(input("Введите номер оценки для пересдачи: "))
            while index < 0 or index >= len(scores):
                print("Неверный номер. Пожалуйста, введите верный номер.")
                index = int(input("Введите номер оценки для пересдачи: "))
            new_score = float(input("Введите новую оценку: "))
            while new_score < 1 or new_score > 12:
                print("Неверная оценка. Пожалуйста, введите оценку между 1 и 12.")
                new_score = float(input("Введите новую оценку: "))
            scores[index] = new_score
        elif choice == '3':
            average = sum(scores) / len(scores)
            if average >= 10.7:
                print("Стипендия выдана.")
            else:
                print("Стипендия не выдана.")
        elif choice == '4':
            sort_order = input("Введите 'возрастание' или 'убывание': ")
            if sort_order.lower() == 'возрастание':
                scores.sort()
            elif sort_order.lower() == 'убывание':
                scores.sort(reverse=True)
            else:
                print("Неверный порядок сортировки. Пожалуйста, введите 'возрастание' или 'убывание'.")
            print(scores)
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Пожалуйста, введите номер между 1 и 5.")


if __name__ == '__main__':
    main()