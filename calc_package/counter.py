class Calculator:
    """A class which main function is to calculate numbers.
    It can do addition, subtraction, multiplication, division,
    as well as take (n) root of a number.
    Functions are: 
    add(x, y) - for addition;
    sub(x, y) - for subtraction;
    mul(x, y) - for multiplication;
    div(x, y) - for division;
    roo(x, y) - to take a root with selected level(y). roo(x, 2) would be square root;
    memory() - returns last calculated number;
    reset() - resets number to 0"""

    def __init__(self):
        self.memory = 0

    def add(self, x, y):
        result = x + y
        self.memory = result
        return result

    def sub(self, x, y):
        result = x - y
        self.memory = result
        return result    

    def mul(self, x, y):
        result = x * y
        self.memory = result
        return result

    def div(self, x, y):
        try:
            result = x / y
        except ZeroDivisionError as zdr:
            print('\nZero division cannot be done! Use different number. \nError name: ', zdr)
        else:
            self.memory = result
            return result
    
    def roo(self, x, y):
        result = x **(1/y) #---To select root with certain level formula is: x ** (1/n), where n is level of the root.---
        self.memory = result
        return result

    def memory(self):
        return self.memory
    
    def reset(self):
        self.memory = 0


# result = Calculator(0)
# while True:
#     i = input()
#     if i.startswith('+'):
#         addition = float(i[1:])
#         print(result.add(addition))
#     elif i.startswith('-'):
#         subtraction = float(i[1:])
#         print(result.sub(subtraction))
#     elif i.startswith('*'):
#         multiplication = float(i[1:])
#         print(result.mul(multiplication))
#     elif i.startswith('/'):
#         division = float(i[1:])
#         print(result.div(division))
#     elif i.startswith('r'):
#         root = float(i[1:])
#         print(result.roo(root))
#     elif i == 'c':
#         break
#     else:
#         break
    