public class Main{
    public static void sortInExample(int[] myArray){
        int minVal = myArray[0];

        for (int i : myArray){
            if (i < minVal){
                minVal = i;
            }
        }
        System.out.println("Lowest value: " + minVal);
    }
    
    public static void main(String[] args){
        sortInExample(new int[] {7, 12, 9, 4, 11});
        sortInExample(new int[] {3, 5, 2, 1});
    }

}