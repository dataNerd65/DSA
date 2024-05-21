class Solution:
    def __init__(self, myArray):
        self.myArray = myArray

    def bubbleSort(self):
        n = len(self.myArray)
        for i in range(n-1):
            for j in range(n - i - 1):
                if self.myArray[j] > self.myArray[j+1]:
                    self.myArray[j], self.myArray[j+1] = self.myArray[j+1], self.myArray[j]


        print(f"Sorted Array: {self.myArray}")

s = Solution([64, 34, 25, 12, 22, 11, 90, 5])
s.bubbleSort()

        