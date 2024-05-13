public class Redo {
    public static void SortArray(int[] array){
        int miniVal = array[0];

        for (int i : array){
            if (i < miniVal){
                miniVal = i;
            }

        }
        System.out.println("FirstNo." + miniVal);
//Logic of printing the arrays...
        int n = array.length;
        for (int k = 0; k < n-1; k++){
            for (int j = 0;  j < n-k-1; j++){
                if (array[j] > array[j+1]){ // Was missing this statement
                //Swapping array[j] and array[j+1]
                int temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    }
        //printing the sorted array
        System.out.print("Sorted Array: ");//Using print statement to print the numbers of array in oneline
        for(int num: array){
            System.out.print(num + " ");
        }
        System.out.println();
        
    }
    //...In one line and sorted

    public static void main(String[] args){
        SortArray(new int[] {7, 12, 9, 4, 11});
        SortArray(new int[] {5, 19, 3, 40, 11});
    }

}
