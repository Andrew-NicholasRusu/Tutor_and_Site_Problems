package RegistryGroup;/*
Task 2: The Behavioral Interface
 */

// Create an interface named Inspected
public interface Inspected {

// Method: boolean runSafetyCheck(). 
// (This represents a pass/fail safety inspection).

    public default boolean runSafetyCheck() {
        return true;
    }
}
