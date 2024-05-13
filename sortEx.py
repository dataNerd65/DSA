class SortEx:
    def SortInExample():
      my_array= [7, 12, 9, 4, 11]

      minVal = my_array[0]

      for i in my_array:
         if i < minVal:
            minVal = i

      print(f'Lowest value:  {minVal}')

SortEx.SortInExample()