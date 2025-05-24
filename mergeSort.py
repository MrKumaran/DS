"""
Divide all component vitually into small i.e one elem
Then upon merging them sort.
"""

def mergeSort(arr, left, right):
    if left < right:
        mid = (right + left) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid+1, right)
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    left_arry = arr[left:mid+1]
    right_arry = arr[mid+1:right+1]
    i = 0
    j = 0
    k = left
    while i < len(left_arry) or j < len(right_arry):
        if i < len(left_arry):
            if j < len(right_arry):
                if left_arry[i] >= right_arry[j]:
                    arr[k] = right_arry[j]
                    k+=1
                    j+=1
                else:
                    arr[k] = left_arry[i]
                    k+=1
                    i+=1
            else:
                arr[k] = left_arry[i]
                k+=1
                i+=1
        else:
            arr[k] = right_arry[j]
            k+=1
            j+=1

n = 10
arr = [3, 7, 1, 9, 2, 6, 10, 5, 4, 8]
mergeSort(arr, 0, n-1)
print(arr)
