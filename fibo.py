class Fibo:
    def Fibonacci():
        prev_1 = 0
        prev = 1

        print(prev_1)
        print(prev)

        for fibo in range(18):
            newFibo = prev + prev_1
            print(newFibo)
            prev_1 = prev
            prev = newFibo

Fibo.Fibonacci()
