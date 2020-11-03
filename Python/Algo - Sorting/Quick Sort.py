def quicksort(array,left,right):
    if left < right:
        pivot = right
        partionIndex = partition(array,left,right,pivot)

        quicksort(array,left,partionIndex-1)
        quicksort(array,partionIndex+1,right)
    return array

def partition(array,left,right,pivot):
    pivotvalue = array[pivot]
    partitionIndex = left

    for i in range(left,right):
        if array[i] < pivotvalue:
            swap(array,i,partitionIndex)
            partitionIndex += 1

    swap(array,right,partitionIndex)
    return partitionIndex

def swap(array,firstIndex,secondIndex):
    array[firstIndex], array[secondIndex] = array[secondIndex], array[firstIndex]

numbers = [48,21,30,5,99,60,36,12,78,56]
sorted_array = quicksort(numbers,0,len(numbers)-1)
print(sorted_array)

numbers_2 = [99,44,6,21,1,5,63,87,283,4,0]
sorted_array_2 = quicksort(numbers_2,0,len(numbers_2)-1)
print(sorted_array_2)