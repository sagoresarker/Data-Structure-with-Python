def merge(list1, list2):
    combined = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined


def merge_sort(myList):
    if len(myList) == 1:
        return myList
    mid_index = int(len(myList) / 2)
    left = merge_sort(myList[:mid_index])
    right = merge_sort(myList[mid_index:])

    return merge(left, right)


values = [4, 2, 6, 5, 1, 3, 9, 56, 3, 1, 11]


print(merge_sort(values))
