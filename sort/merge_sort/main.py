import numpy as np

def mergeSort(arr):
    if len(arr) > 1:
        division = len(arr) // 2
        left = arr[:division].copy()
        right = arr[division:].copy()

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


print(mergeSort(np.array([5, 45, 6, 2, 22, 88, 99, 74, 32, 21, 34, 24, 55])))
