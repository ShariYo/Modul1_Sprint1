class Calculator:
    def __init__(self, number):
        self.number = number

    def add(self, num):
        self.number = self.number + num
        return self.number
    
    def sub(self, num):
        self.number = self.number - num
        return self.number
    
    def mul(self, num):
        self.number = self.number * num
        return self.number
    
    def div(self, num):
        self.number = self.number / num
        return self.number
    
    def roo(self, num):
        self.number = self.number **(1/num)
        return self.number

result = Calculator(0)
while True:
    i = input()
    if i.startswith('+'):
        addition = float(i[1:])
        print(result.add(addition))
    elif i.startswith('-'):
        subtraction = float(i[1:])
        print(result.sub(subtraction))
    elif i.startswith('*'):
        multiplication = float(i[1:])
        print(result.mul(multiplication))
    elif i.startswith('/'):
        division = float(i[1:])
        print(result.div(division))
    elif i.startswith('r'):
        root = float(i[1:])
        print(result.roo(root))
    elif i == 'c':
        break
    else:
        break
    




# n root will be x**(1/n)