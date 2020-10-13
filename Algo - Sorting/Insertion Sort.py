def insertionSort(array):
    n = len(array)
    for i in range(n):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1],array[i]
        for j in range(i,0,-1):
            if array[j] < array[j-1]:
                array[j-1], array[j] = array[j], array[j-1]
    return array

numbers = [48,21,30,5,99,60,36,12,78,56]
sorted_array = insertionSort(numbers)
print(sorted_array)

numbers_2 = [99,44,6,21,1,5,63,87,283,4,0]
sorted_array_2 = insertionSort(numbers_2)
print(sorted_array_2)
