class Solution: 
    def select(self, arr, i):
        smallest = arr[0]
        smallest_index = 0
        for j in range(i,len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_index= j
        return smallest_index
    
    def selectionSort(self, arr,n):
        sorted_array = []
        for i in range(len(arr)):
            smallest = self.select(arr,n-1)
            sorted_array.append(arr.pop(smallest))
        return sorted_array