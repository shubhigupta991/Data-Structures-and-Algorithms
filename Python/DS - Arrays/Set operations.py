''' Set operations
1. `union
2. `intersection`
3. `difference
4. `set membership` '''

def union(array1,array2):
    # if the arrays are not sorted                     complexity = m + m*n = O(n^2)
    union_array = []
    for element in array1:
        union_array.append(element)
    for element in array2:
        if element not in union_array:
            union_array.append(element)
        else:
            continue
    return union_array

def sorted_union(array1,array2):
    # if the arrays are sorted                        complexity = m + n = O(n)
    union_array = []
    i, j  = 0,0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            union_array.append(array1[i])
            i += 1
        elif array1[i] > array2[j]:
            union_array.append(array2[j])
            j += 1
        else:
            union_array.append(array1[i])
            i += 1
            j += 1
    return union_array + array1[i:] + array2[j:]

def intersection(array1,array2):
    # if the arrays are not sorted                     complexity = m*n = O(n^2)
    intersection_array = []
    for element in array1:
        if element in array2:
            intersection_array.append(element)
    return intersection_array

def sorted_intersection(array1,array2):
    # if the arrays are sorted                        complexity = m + n = O(n)
    intersection_array = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            i += 1
        elif array1[i] > array2[j]:
            j += 1
        elif array1[i] == array2[j]:
            intersection_array.append(array1[i])
            i += 1
            j += 1
    return intersection_array

arr1 = [3,5,10,4,6]
arr2 = [12,4,7,2,5]
arr3 = [3,4,5,6,10]
arr4 = [2,4,5,7,12]

print(union(arr1,arr2))
print(intersection(arr1,arr2))
print(sorted_union(arr3,arr4))
print(sorted_intersection(arr3,arr4))