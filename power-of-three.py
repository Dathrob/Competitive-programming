def powerofthree(num):
    if (((num / 3) == 1) or num == 1):
        return True
    elif num % 3 != 0 or num == 0:
        return False
    else:
        return powerofthree(num/3)
print(powerofthree(3486784401))