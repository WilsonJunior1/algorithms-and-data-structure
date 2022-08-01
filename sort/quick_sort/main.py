import numpy as np

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

def quickSort(arr, start, end):
    if start < end:
        position = partition(arr, start, end)

        quickSort(arr, start, position - 1)
        quickSort(arr, position + 1, end)
    return arr


arr = np.array([10, 23, 54, 55, 22, 56, 83, 21, 14, 19, 72, 43])
print(quickSort(arr, 0, len(arr) - 1))
