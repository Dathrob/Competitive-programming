#10 minutes
def sortcolors(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:]if i <= pivot]
        greater = [i for i in array[1:]if i > pivot]
        return sortcolors(less) + [pivot] + sortcolors(greater)
print(sortcolors([2,0,1]))