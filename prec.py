class SortInArray:
    def SortArray(arr):
        #arr = (20, 4, 1, 8, 9,56)

        FirstNo = arr[0]

        for i in arr:
            if i < FirstNo:
                FirstNo = i

        print(f"FirstNo:  {FirstNo}")

        

SortInArray.SortArray([20, 4, 1, 8, 9, 56])