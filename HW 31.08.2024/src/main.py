def SortList(lst):
    if not isinstance(lst, list):
        raise TypeError("Input should be a list")

    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


lst = [5, 3, 8, 6, 7, 2]

if __name__ == "__main__":
    print(SortList(lst))
