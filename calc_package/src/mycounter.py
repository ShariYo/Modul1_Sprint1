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




#---Just for fun I made my automated calculator version with implemented Calculator class methods.---

# result = Calculator()
# while True:
#         i = input()
#         if i.startswith('+'):
#             result.add(result.memory, float(i[1:]))
#             print(f'\nResult: {result.memory}')
#         elif i.startswith('-'):
#             result.sub(result.memory, float(i[1:]))
#             print(f'\nResult: {result.memory}')
#         elif i.startswith('*'):
#             result.mul(result.memory, float(i[1:]))
#             print(f'\nResult: {result.memory}')
#         elif i.startswith('/'):
#             result.div(result.memory, float(i[1:]))
#             print(f'\nResult: {result.memory}')
#         elif i.startswith('r'):
#             """This r letter, entering r and number by it (e.g. r2) takes selected level root."""
#             result.roo(result.memory, float(i[1:]))
#             print(f'\nResult: {result.memory}')
#         elif i == 'c':
#             """This c letter, after entering it into calculator, resets memory."""
#             result.reset()
#             print(f'\nResult: {float(0)}')
#         elif i.startswith('s'):
#             """Stops calculator completely."""
#             print('\nYou have stopped calculating.')
#             break
#         else:
#             print(f'There was Value Error: {ValueError}. Please insert number, not a string!')