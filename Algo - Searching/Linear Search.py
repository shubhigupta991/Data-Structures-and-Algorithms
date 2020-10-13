def linearSearch(array,value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    else:
        return "Not Found"

arr = [5,2,7,3,9,8,0,4,6,10]
print(linearSearch(arr,7))
print(linearSearch(arr,55))