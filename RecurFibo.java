public class RecurFibo{
    static int count = 2;//indicates that a particular member(variable, method, or inner class) belongs to the class itself rather than to an instance of the class
    public static void Fibonacci(int prev1, int prev2){
        if(count <= 19){
            int newFibo = prev1 + prev2;
            System.out.println(newFibo);
            prev2 = prev1;
            prev1 = newFibo;
            count += 1;
            Fibonacci(prev1, prev2);
        }else {
            return;
        }
    }

    public static void main(String[] args){
        System.out.println(0);
        System.out.println(1);
        Fibonacci(1,0);
    }
}