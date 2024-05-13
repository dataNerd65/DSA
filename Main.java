public class Main{
    private int[] myArray;

    public Main(int[] myArray){
        this.myArray = myArray;
    }
    public  void sortInExample(){
        int minVal = myArray[0];

        for (int i : myArray){
            if (i < minVal){
                minVal = i;
            }
        }
        System.out.println("Lowest value: " + minVal);
    }
    public static void main(String[] args){
      Main instance1 = new Main(new int[] {7, 12, 9, 4, 11});
        instance1.sortInExample();

      Main instance2 = new Main(new int[] {3, 5, 2, 1});
      instance2.sortInExample();

         
    }

}