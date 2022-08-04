import numpy as np

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr

print(bubble_sort(np.array([20, 45, 10, 5, 3, 2, 25, 50, 60, 55, 1, 0, 99])))
