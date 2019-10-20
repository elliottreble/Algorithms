#MergeSort takes an unstorted list and sorts it increasingly


def MergeSort(list, left, right):
    if(left < right):
        middle = (left+right)/2
        MergeSort(list, left, middle)
        MergeSort(list, middle, right)
        print(list)
        Merge(list, left, middle, right)


def Merge(list, left, middle, right):
    s1 = middle - left + 1
    s2 = right - middle

    leftArray = []
    rightArray = []

    i = 0

    while i < s1:
        leftArray[i] = list[left + i]
        i += 1

    i = 0

    while i < s2:
        rightArray[i] = list[middle + 1 + i]
        i += 1
    i = 0
    j = 0

    k = left

    while i < s1 and j < s2:
        if leftArray[i] < rightArray[j]:
            list[k] = leftArray[i]
            k += 1
            i += 1
        else:
            list[k] = rightArray[j]
            k += 1
            j += 1

    while i < s1:
        list[k] = leftArray[i]
        k += 1
        i += 1

    while j < s2:
        list[k] = rightArray[j]
        k += 1
        j += 1

list = [1,6,0,8,12,22,45,7,99,100,11,10,20,26,38,201,13,4,3]
MergeSort(list, 0, len(list) - 1)
print(list)
