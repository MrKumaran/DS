"""
start from second and find the min value from previous
i.e from index 0 to current element
if small element it shift everything and place element.
"""

def selectionSort(arr):
    for i in range(len(arr)):
        mini = arr[i]
        index = i
        for j in range(i,len(arr)):
            if mini > arr[j]:
                mini = arr[j]
                index = j
        arr[i],arr[index] = arr[index],arr[i]
        prinIteration(arr)

def selectionSortDESC(arr):
    for i in range(len(arr)):
        maxi = arr[i]
        index = i
        for j in range(i,len(arr)):
            if maxi < arr[j]:
                maxi = arr[j]
                index = j
        arr[i],arr[index] = arr[index],arr[i]
        prinIteration(arr)

def prinIteration(arr):
    print(arr)


n = 10
arr = [3, 7, 1, 9, 2, 6, 10, 5, 4, 8]
selectionSort(arr)
selectionSortDESC(arr)
