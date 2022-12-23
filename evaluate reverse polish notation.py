from collections import deque
def calculate(array):
    stack = deque()
    num = ["1","2","3","4","5","6","7","9","0"]
    calculator = ["+","-","/","*"]
    for i in array:
        if i in num:
            stack.append(i)
        else:
            if i == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif i == "-":
                stack.append(int(stack.pop()) - int(stack.pop()))
            elif i == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            else:
                stack.append(int(stack.pop()) / int(stack.pop()))
            
    return stack[-1]

print(calculate(["2","1","+","3","*"]))