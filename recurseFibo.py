class FiboInRecurse:
    def __init__(self, num):
        self.num = num

    def F(self, num):
        if num <= 1:
            return num
        else:
            return self.F(num-1) + self.F(num-2)
            
    def print_fibonacci(self):
        print(self.F(self.num))

fibo = FiboInRecurse(19)
fibo.print_fibonacci()
            
            
    