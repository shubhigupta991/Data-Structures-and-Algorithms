def selectionSort(array):
    n = len(array)
    for i in range(n):
        minimum = array[i]
        pos = i
        for j in range(i+1,n):
            if array[j] < minimum:
                minimum = array[j]
                pos = j
        array[i] , array[pos] = array[pos] , array[i]
    return array

numbers = [48,21,30,5,99,60,36,12,78,56]
sorted_array = selectionSort(numbers)
print(sorted_array)

numbers_2 = [99,44,6,21,1,5,63,87,283,4,0]
sorted_array_2 = selectionSort(numbers_2)
print(sorted_array_2)