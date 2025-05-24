"""
List is sep into 2 part one sorted another is unsorted
first start from second element index 1.
assume element 1 is sorted.
now compare the pivot element(index 1) and compare from index 0 to till pivot index
and place it in correct index by shifting other elements if needed.
"""

def insectionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
        prinIteration(arr)

def insectionSortDESC(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
        prinIteration(arr)

def prinIteration(arr):
    print(arr)


n = 10
arr = [3, 7, 1, 9, 2, 6, 10, 5, 4, 8]
insectionSort(arr)
insectionSortDESC(arr)
