public class Recursion_Practice_2 {

    public static int factorial(int n) {
        int result = -1;
        if ( n < 0) { // this is the error case
            System.out.println("Factorial is not defined for negative numbers!");
        } else if (n == 0) { // this is the base case
            result = 1;
        } else { // case if (n > 0) // this is the general case
            result = n * factorial(n - 1); // recursive call
        }
        return result;
    }

    public static void main(String[] args) {
    
    }
}
