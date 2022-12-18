'''
taken 25 minutes

'''
def fibonacci(num):
    if (num <= 1):
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
print(fibonacci(5))