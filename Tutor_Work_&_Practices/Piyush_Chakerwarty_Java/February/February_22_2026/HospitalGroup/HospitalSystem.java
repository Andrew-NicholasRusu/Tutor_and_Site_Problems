package HospitalGroup;

public class HospitalSystem {
    public static void main(String[] args) {

        // Storage: Create an array of type HospitalStaff with a size of 2.
        HospitalStaff[] HospitalStaff = new HospitalStaff[2];

        // Populate: 
        // Index 0: A Surgeon ("Dr. Smith", 101). 
        // Index 1: A MedicalRobot ("Unit-X", 505). 
        HospitalStaff[0] = new Surgeon("Dr.Smith", 101);
        HospitalStaff[1] = new MedicalRobot("Unit-X", 505);

        // Iterate through the array and call displayBadge() and performDuty() for every item. 
        for (int i = 0; i < HospitalStaff.length; i ++) {
            HospitalStaff[i].displayBadge();
            HospitalStaff[i].performDuty();
        }

        // Polymorphic Logic: Use instanceof to check if the staff member is a Surgeon. If so, cast it and call scrubIn(). 
        if (HospitalStaff[0] instanceof Surgeon) {
            Surgeon surgeon = (Surgeon) HospitalStaff[0];
            surgeon.scrubIn();
        }

        // Interface Logic: Use instanceof to check if the item is Sanitizable. If it is, cast it and call performSanitization(). 
        if (HospitalStaff[1] instanceof Sanitizable) {
            Sanitizable sanitizable = (Sanitizable) HospitalStaff[1];
            sanitizable.performSanitization();
        }
        System.out.println();
    }
}
