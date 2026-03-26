package RegistryGroup;/*
Task 1: The Abstract Foundation
 */

// Create an abstract class named RegistryItem. 
public abstract class RegistryItem {

    // Attributes: protected String registrationId and protected double baseValue. 
    protected String registrationId;
    protected double baseValue;

    // Constructor: A constructor that initializes both fields. 
    public RegistryItem(String registrationId, double baseValue) {
        this.registrationId = registrationId;
        this.baseValue = baseValue;
    }

    // Getters and Setters
    public String getRegistrationId() {
        return registrationId;
    }

    public void setRegistrationId(String registrationId) {
        this.registrationId = registrationId;
    }

    public double getBaseValue() {
        return baseValue;
    }

    public void setBaseValue(double baseValue) {
        this.baseValue = baseValue;
    }

    // Abstract Method: public abstract double calculateTax(). (Each vehicle type calculates tax differently).
    public abstract double calculateTax();

    // Final Method: public final void printReceipt(). 
    // This should print: "Receipt for ID: [registrationId] | Final Amount: $[calculatedTax]"
    public final void printReceipt() {
        System.out.println("Receipt for ID: [" +  registrationId + "] Final Amount: $[" + baseValue + "]");
    }

    

}
