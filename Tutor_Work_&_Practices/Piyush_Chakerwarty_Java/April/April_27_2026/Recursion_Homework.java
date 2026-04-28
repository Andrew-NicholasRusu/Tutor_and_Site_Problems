// Write a program to find the sum of all the numbers between one to N.  
// Take N as an input from the user.  

import java.util.Scanner;
public class Recursion_Homework {
    Scanner sc = new Scanner(System.in);

    public static int factorial(int n) {
        if (n <= 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }

    public static void main(String[] args) {
        
    }
    

}
