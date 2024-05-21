public class Bubble1{
    public static void main(String[] args){
        int[] myArray = {64, 34, 25, 12, 22, 11, 90, 5};

        int n = myArray.length;

        for(int i = 0; i < n-1; i++){
            for(int j = 0; j < n-i-1; j++){
                if (myArray[j] > myArray[j+1]){
                    int temp = myArray[j];
                    myArray[j] = myArray[j+1];
                    myArray[j+1] = temp;

                }
            }
        }
        System.out.print("Sorted Array: ");
        for (int i = 0; i < n; i++){
            System.out.print(myArray[i] + " ");

        }
        System.out.println();
    }
}