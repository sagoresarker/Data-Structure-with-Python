def selectionSort(values):
    for i in range(len(values) - 1):
        min_index = i
        for j in range(i + 1, len(values)):
            if values[j] < values[min_index]:
                min_index = j
        if i != min_index:
            temp = values[i]
            values[i] = values[min_index]
            values[min_index] = temp
    return values


values = [4, 2, 6, 5, 1, 3]

print(selectionSort(values))
