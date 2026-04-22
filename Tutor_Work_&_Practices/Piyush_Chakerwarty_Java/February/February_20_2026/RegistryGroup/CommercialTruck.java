package RegistryGroup;/*
Task 3: The Concrete Subclasses
Class A: CommercialTruck
*/

// Inheritance: Extends RegistryItem and implements Inspected. 
public class CommercialTruck extends RegistryItem implements Inspected {
    // New Attribute: private double tonnage. 
    private double tonnage;

    public CommercialTruck(String registrationId, double baseValue, double tonnage) {
        super(registrationId, baseValue);
        this.tonnage = tonnage;
    }

    // Getter and Setter
    public double getTonnage() {
        return tonnage;
    }

    public void setTonnage(double tonnage) {
        this.tonnage = tonnage;
    }

    @Override
    public double calculateTax() {
        return (this.baseValue * 0.15) + (this.tonnage * 50);
    }

    // runSafetyCheck(): Simply print "Checking brakes and weight limits..." and return true.  
    @Override
    public boolean runSafetyCheck() {
        System.out.println("Checking brakes and weight limits...");
        return true;
    }

}
