class RecurFibo:
    #
    def __init__(self):

        self.count = 2

    def fibonaci(self, prev1, prev2): #when calling this method recursively, use self.fibonacci
        global count #Calling the globally initialized count variable

        if self.count <= 19:
            newFibo = prev1 + prev2
            print(newFibo)
            prev2 = prev1
            prev1 = newFibo
            self.count += 1

            self.fibonaci(prev1, prev2)
        else:
            return
        
fibo = RecurFibo()
print(0)
print(1)
fibo.fibonaci(1, 0)



