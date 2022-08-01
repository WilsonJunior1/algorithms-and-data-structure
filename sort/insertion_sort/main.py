import numpy as np

def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        mark = arr[i]

        j = i - 1
        while j >= 0 and mark < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = mark

    return arr

print(insertionSort(np.array([14, 26, 12, 76, 23, 11, 2, 7, 99, 88, 42])))
