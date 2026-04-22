// You are programming a robotic arm for a narrow delivery truck. The truck is so narrow that boxes must be stacked one in front of the other. 
// Therefore, the last box loaded into the truck must be the first one unloaded. 

// Your Task: Create a class called CargoLoader that uses a Stack<String> to manage the delivery boxes. You must implement the following 
// operations using the specific methods from the Stack class: 
    // 1. loadBox(String boxName): Adds a new box to the top of the stack. 
    // 2. checkNextToUnload(): Looks at the box currently at the door (the top of the stack) without removing it. 
    // 3. unloadBox(): Removes and returns the box at the door. If the truck is empty, return a warning message. 
    // 4. findBoxDepth(String boxName): The driver needs to know how far back a specific box is. Use the stack's search function to return its 1-based position from the top. 
    // 5. isTruckEmpty(): Returns true if all boxes have been unloaded. 

import java.util.Stack;

public class CargoLoader {
    Stack<String> management = new Stack<>();

    public void loadBox(String boxName) {
        management.addFirst("Robotz"); // Adds a new box to the top 
    }

    public void checkNextToUnload() {
        management.size();
    }

    public String unloadBox() {
        management.removeFirst();
        if (management.isEmpty()) {
            return "Warning: Can't unload because it's empty.";
        }
        return ""; // Returns to the box at the door. 
    }

    public void findBoxDepth(String boxName) {
        int position = management.search(boxName);
        System.out.println(position + 1); // returns its 1-based position from the top
    }

    public boolean isTruckEmpty() { 
        if (management.isEmpty()) {
            return true; // Returns true if all boxes have been unloaded
        } else {
            return false;
        }
    }

    public static void main(String[] args) {
        CargoLoader cargoLoader = new CargoLoader();
        System.out.println("Loading a robotic arm process:");

        // Loads what box to pick:
        cargoLoader.loadBox("boxName");

        // Checking the next box:
        System.out.println("Checking the next box:");
        cargoLoader.checkNextToUnload();

        // Unloading the box:
        System.out.println("Unloading the box:" + cargoLoader.unloadBox());

        // Finding the box depth:
        System.out.println("Finding the box depth:");
        cargoLoader.findBoxDepth("Robotz");

        // Checks if the truck is empty:
        System.out.println(cargoLoader.isTruckEmpty());
    }
}
