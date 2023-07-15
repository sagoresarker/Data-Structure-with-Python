def insertion_sort(values):
    for i in range(1, len(values)):
        temp = values[i]
        j = i - 1
        while temp < values[j] and j > -1:
            values[j + 1] = values[j]
            values[j] = temp
            j -= 1
        return values


values = [1, 2, 4, 3, 5, 6]
print(insertion_sort(values))
