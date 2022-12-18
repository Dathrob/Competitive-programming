'''
5 minutes
'''
def poweroffour(num):
    if (((num / 4) == 1) or num == 1):
        return True
    elif num % 4 != 0 or num == 0:
        return False
    else:
        return poweroffour(num/4)
print(poweroffour(1))