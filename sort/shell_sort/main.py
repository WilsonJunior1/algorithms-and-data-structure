import numpy as np

def shellSort(arr):
    interval = len(arr) // 2

    while interval > 0:
        for i in range(interval, len(arr)):
            temp = arr[i]
            j = i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval
            arr[j] = temp
        interval //= 2
    return arr

print(shellSort(np.array([1, 5, 2, 3, 56, 61, 98, 12, 52, 35, 90, 17 ,23]))) 
