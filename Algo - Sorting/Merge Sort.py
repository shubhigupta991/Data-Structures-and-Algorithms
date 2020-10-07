def mergeSort(array):
    n = len(array)
    if n == 1:
        return array
    mid = n // 2
    left = array[:mid]
    right = array[mid:]
    return merge(
        mergeSort(left),
        mergeSort(right)
    )

def merge(left,right):
    i = 0
    j = 0
    result = []
    while i<len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]

numbers = [48,21,30,5,99,60,36,12,78,56]
sorted_array = mergeSort(numbers)
print(sorted_array)

numbers_2 = [99,44,6,21,1,5,63,87,283,4,0]
sorted_array_2 = mergeSort(numbers_2)
print(sorted_array_2)