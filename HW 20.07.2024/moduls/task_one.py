'''
Задание № 1
Реализуйте класс стека для работы со строками(стек строк). Стек должен иметь фиксированный размер. Реализуйте набор
операций для работы со стеком:
    - помещение строки в стек;
    - выталкивание строки из стека;
    - подсчет количества строк в стеке;
    - проверку пустой ли стек.
    - проверку полный ли стек.
    - очистку стека.
    - получение значения без выталкивания верхней строки из стека. При старте приложения нужно отобразить меню с
    помощью, которого пользователь может выбрать необходимую операцию.
'''


class StringStack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []

    def push(self, string: str) -> None:
        if self.is_full():
            raise ValueError("Стек уже полный")
        self.stack.append(string)

    def pop(self) -> str:
        if self.is_empty():
            raise ValueError("Стек уже пуст")
        return self.stack.pop()

    def size(self) -> int:
        return len(self.stack)

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def is_full(self) -> bool:
        return len(self.stack) == self.capacity

    def clear(self) -> None:
        self.stack.clear()

    def peek(self) -> str:
        if self.is_empty():
            raise ValueError("Стек пуст")
        return self.stack[-1]

    def menu(self) -> None:
        print("1 - поместить строку в стек")
        print("2 - вытолкнуть строку из стека")
        print("3 - подсчет количества строк в стеке")
        print("4 - проверка пустой ли стек")
        print("5 - проверка полный ли стек")
        print("6 - очистка стека")
        print("7 - получить значение верхней строки без выталкивания")
        print("8 - выход")
        while True:
            try:
                choice = int(input("Выберите действие: "))
                if choice == 1:
                    string = input("Введите строку: ")
                    self.push(string)
                elif choice == 2:
                    print(self.pop())
                elif choice == 3:
                    print(self.size())
                elif choice == 4:
                    print(self.is_empty())
                elif choice == 5:
                    print(self.is_full())
                elif choice == 6:
                    self.clear()
                elif choice == 7:
                    print(self.peek())
                elif choice == 8:
                    break
            except ValueError as e:
                print(str(e))
            except Exception as e:
                print("Произошла непредвиденная ошибка:", str(e))



