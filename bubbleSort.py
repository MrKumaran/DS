"""
compare next element if small swap
"""

def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        prinIteration(arr)


def bubbleSortDESC(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] < arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        prinIteration(arr)


def prinIteration(arr):
    print(arr)


n = 10
arr = [3, 7, 1, 9, 2, 6, 10, 5, 4, 8]
bubbleSort(arr)
bubbleSortDESC(arr)
