package BirdGroup;

public class BirdMain {
    public static void main(String[] args) {

        // Creating the objects
        Bird penguin1 = new Penguin("Black and White", "Penguin", false, "Male");
        Bird eagle1 = new Eagle("White", "Eagle", true, "Male");
        Bird turkey1 = new Turkey("Brown", "Turkey", false, "Male");

        // Array to store the classes
        Bird[] birdGroup = new Bird[3];

        // Storing the objects in the method
        birdGroup[0] = penguin1;
        birdGroup[1] = eagle1;
        birdGroup[2] = turkey1;

        // Make a nested loop that will print out the objects.
        for (Bird bird : birdGroup) {
            System.out.println(bird);
        }

        
        
        
    }   
}

