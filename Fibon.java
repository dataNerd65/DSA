//Creating a fibonacci code to get fibonacci using java
public class Fibon {
    public static void main(String[] args){
        int prev2 = 0;
        int prev1 = 1;

        System.out.println(prev2);
        System.out.println(prev1);

        for (int fibo = 0; fibo < 18; fibo++){
            int NewFibo = prev1 + prev2;
            System.out.println(NewFibo);
            prev2 = prev1;
            prev1 = NewFibo;
            
        }

    }

}
