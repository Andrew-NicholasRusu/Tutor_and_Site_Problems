package RegistryGroup;/*
Class B: ElectricCar 
*/

// Inheritance: Extends RegistryItem (No inspection required for this specific tax-exempt class). 
public class ElectricCar extends RegistryItem {

public ElectricCar(String registrationId, double baseValue) {
        super(registrationId, baseValue);
        
    }

    // calculateTax(): Return baseValue * 0.05 (Lower tax for green vehicles). 
    @Override
    public double calculateTax() {
        return this.baseValue * 0.05;
        // Lower tax for green vehicles
    }

}
