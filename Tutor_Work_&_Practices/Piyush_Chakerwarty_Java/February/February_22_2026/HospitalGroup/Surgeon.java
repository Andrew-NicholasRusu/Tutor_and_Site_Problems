package HospitalGroup;

// Subclass
public class Surgeon extends HospitalStaff {

    public Surgeon(String name, int staffId) {
        super(name, staffId);
    }

    // Implementation: 
    // performDuty(): Print "Surgeon [name] is performing a specialized surgery." 
    @Override
    public void performDuty(){
        System.out.println("Surgeon " + name + " is performing a specialized surgery.");
    }

    // Unique Feature: Add a method scrubIn() that prints 
    // "Surgeon is preparing for the operating room." 
    public void scrubIn() {
        System.out.println("Surgeon is preparing for the operating room.");
    }

}
