""" Задание 3. Напишите функцию, определяющую количество простых чисел в списке целых. Список передаётся в качестве
параметра.Полученный результат возвращается из функции. """

def search_prime_numbers(send_list):
    primes = []
    for item in send_list:
        if item == 2:
            primes.append(item)
        elif item == 1:
            continue
        else:
            is_prime = True
            for i in range(2, item):
                if item % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(item)
    return print(len(primes))
