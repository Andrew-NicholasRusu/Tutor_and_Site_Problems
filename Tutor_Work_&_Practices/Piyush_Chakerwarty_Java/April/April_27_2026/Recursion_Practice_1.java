public class Recursion_Practice_1 {
    public static int factorial(int n) {
        if (n <= 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }

    public static void main(String[] args) {
        int number = 5;
        int number2 = 4;
        int number3 = 3;
        int number4 = 1;
        System.out.println("Factorial of number: " + number + " is " + factorial(number)); // 5 * 4 * 3 * 2 * 1 = 120
        System.out.println("Factorial of number: " + number2 + " is " + factorial(number2)); // 4 * 3 * 2 * 1 = 24
        System.out.println("Factorial of number: " + number3 + " is " + factorial(number3)); // 3 * 2 * 1 = 6
        System.out.println("Factorial of number: " + number4 + " is " + factorial(number4)); // 1


        
    }
}