class Solution:
    def __init__(self, myArray):
        self.myArray = myArray


    def bubbleSortEfficient(self):
        n = len(self.myArray)

        for i in range(n-1):
            swapped = False


            for j in range(n-i-1):
                if self.myArray[j] > self.myArray[j+1]:
                    self.myArray[j], self.myArray[j+1] = self.myArray[j+1], self.myArray[j]

                    swapped = True

            if not swapped:
                break
        print(f"Sorted Array: {self.myArray}")

s = Solution([7, 3, 9, 12, 11])
s.bubbleSortEfficient()
#This is now an efficient bubble sort algorithm