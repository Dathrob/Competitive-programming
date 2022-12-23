class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        list1 = []
        calculator = ["+","-","/","*"]
        for i in tokens:
            if i.isdigit():
                list1.append(int(i))
                
            elif i.lstrip("-").isdigit():
                list1.append((int(i)))
                
            else:
                a = list1.pop()
                b = list1.pop()
                if i == "+":
                    list1.append(b + a)
                elif i == "-":
                    list1.append(b - a)
                elif i == "*":
                    list1.append(b * a)
                else:
                    list1.append(int(b / a))
               
        return list1[-1]