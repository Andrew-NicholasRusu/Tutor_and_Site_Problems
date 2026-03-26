package HospitalGroup;

// You are building a digital portal for a hospital. You need to manage different employees 
// and ensure specific medical devices are tracked properly. 

public abstract class HospitalStaff {
    // Attributes: protected String name and protected int staffId. 
    protected String name;
    protected int staffId;

    // Constructor: A constructor that initializes both fields. 
    public HospitalStaff (String name, int staffId) {
        this.name = name;
        this.staffId = staffId;
    }

    // Abstract Method: public abstract void performDuty(). 
    // (This represents the main task of the staff member). 
    public abstract void performDuty();

    // Concrete Method: public void displayBadge() 
    // which prints: "Staff: [name] | ID: [staffId
    public void displayBadge() {
        System.out.println("Staff: [" + name + "] | ID: [" + staffId + "]");
    }

    


}
