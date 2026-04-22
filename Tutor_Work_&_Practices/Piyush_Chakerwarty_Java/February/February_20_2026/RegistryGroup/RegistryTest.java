package RegistryGroup;

/*
Task 4: The Main Class (Test Runs) 
*/
public class RegistryTest {
    public static void main(String[] args) {
    // 1. Polymorphic Storage: Create an array of type RegistryItem with a size of 2. 
    RegistryItem[] warehouse = new RegistryItem[2];
    
    // 2. Instantiation: 
    // Index 0: A CommercialTruck ("TRK-99", $50000, 5.5 tons). 
    // Index 1: An ElectricCar ("EV-2026", $35000). 

    warehouse[0] = new CommercialTruck("TRK-99", 50000.0, 5.5);
    warehouse[1] = new ElectricCar("EV-2026", 35000.0);

    System.out.println("---Starting Registry Processing---");

    // 3. The Processing Loop: 
    // Iterate through the array. 
    for (RegistryItem item : warehouse) {
        // This calls the FINAL method in the parent, which in turn 
        // calls the OVERRIDDEN calculateTax in the child.

        // For every item, call the printReceipt() method. 
        item.printReceipt();
        
        // Logic Check: Use the instanceof operator. If the item is Inspected, call the runSafetyCheck() method. 
        if (item instanceof Inspected) {
            // We "Downcast" the item to Inspected to access the interface
            Inspected checkableItem = (Inspected) item;
            boolean passed = checkableItem.runSafetyCheck();
            System.out.println("Safety Status: " + (passed ? "PASS" : "FAIL"));
        }
        System.out.println("--------------------------");
        }
    }
}
