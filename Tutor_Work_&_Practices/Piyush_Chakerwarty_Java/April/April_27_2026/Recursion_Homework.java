// Write a program to find the sum of all the numbers between one to N.  
// Take N as an input from the user.  

import java.util.Scanner;
public class Recursion_Homework {
    public static int sum(int N) { // Recursion example:
        if (N <= 1) {
            return 1;
        }
        return N + sum (N - 1); // Calculates the sum of N, which is the value of the user.
        // N - 1 
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Take N as an input fron the user:");
        int N = sc.nextInt();
        System.out.println("Sum of all numbers = " + sum(N));
    }
}
