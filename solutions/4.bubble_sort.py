def bubleSort(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j] = l[j] + l[j + 1]
                l[j + 1] = l[j] - l[j + 1]
                l[j] = l[j] - l[j + 1]
    print(l)

bubleSort([1, 4, 7, 3, 55, 9])