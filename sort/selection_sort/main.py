import numpy as np

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arr[min] > arr[j]:
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
    return arr

print(selectionSort(np.array([44, 33, 15, 10, 12, 65, 25, 99, 83, 13, 7, 2])))
