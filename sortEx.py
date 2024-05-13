class SortEx:
    def SortInExample(my_array):
      #my_array= [7, 12, 9, 4, 11]

      minVal = my_array[0]

      for i in my_array:
         if i < minVal:
            minVal = i

      print(f'Lowest value:  {minVal}')

SortEx.SortInExample([7, 12, 9, 4, 11])#In python, when passing multile values to a function, you should pass them as a list or tuple

SortEx.SortInExample([3, 5, 2, 1])