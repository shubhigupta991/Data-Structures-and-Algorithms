def bubbleSort(array):
    n = len(array)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if array[i] > array[j]:
                array[i], array[j] = array[j],array[i]
    return array

numbers = [48,21,30,5,99,60,36,12,78,56]
sorted_array = bubbleSort(numbers)
print(sorted_array)

numbers_2 = [99,44,6,21,1,5,63,87,283,4,0]
sorted_array_2 = bubbleSort(numbers_2)
print(sorted_array_2)