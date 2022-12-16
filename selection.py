#started at 22:01
#finished at 22:11
def select(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index= i
    return smallest_index
def selectionSort(arr):
    sorted_array = []
    for i in range(len(arr)):
        smallest = select(arr)
        sorted_array.append(arr.pop(smallest))
    return sorted_array
print(selectionSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))