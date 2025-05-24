"""
Find pivot, based on pivot divide arr into two parts.
sort those two parts recursively
pivot is usually last value
"""

def partition(arr, low, high):
    i = low-1
    pi = arr[high]
    for j in range(low, high):
        if arr[j] < pi:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quickSort(arr, low, high):
    prinIteration(arr)
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def partitionDESC(arr, low, high):
    i = low-1
    pi = arr[high]
    for j in range(low, high):
        if arr[j] >= pi:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quickSortDESC(arr, low, high):
    prinIteration(arr)
    if low < high:
        pi = partitionDESC(arr, low, high)
        quickSortDESC(arr, low, pi - 1)
        quickSortDESC(arr, pi + 1, high)


def prinIteration(arr):
    print(arr)

def firstQS(arr, low , high):
    print(arr)
    if low < high:
        pivot = firstPart(arr, low, high)
        firstQS(arr, low, pivot-1)
        firstQS(arr, pivot+1, high)

def firstPart(arr, low, high):
    pivot = arr[low]
    i = high+1
    for j in range(high, low, -1):
        if pivot < arr[j]:
            i-=1
            arr[j],arr[i] = arr[i],arr[j]
    arr[low], arr[i-1] = arr[i-1], arr[low]
    return i-1



n = 10
arr = [3, 7, 1, 9, 2, 6, 10, 5, 4, 8]
quickSort(arr, 0, n-1)
#quickSortDESC(arr, 0, n-1)
#firstQS(arr, 0, n-1)
