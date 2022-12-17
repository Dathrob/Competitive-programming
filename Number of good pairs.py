#10 min taken
def numgood(array):
    good_pair = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if ((array[i]) == (array[j])):
                good_pair += 1
    return good_pair
print(numgood([1,1,1,1]))
