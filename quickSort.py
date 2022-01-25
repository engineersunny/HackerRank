#Quick Sort

def quickSort(arr):
    less = []
    pivotList = []
    more = []

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

quickSort([[1,10,5,25,4,36,48,5,78,7,10]])