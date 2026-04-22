package HospitalGroup;

public class MedicalRobot extends HospitalStaff implements Sanitizable {

    public MedicalRobot (String name, int staffId) {
        super(name, staffId);
    }

    // Implementation: 
    // performDuty(): Print "Robot [ID] is delivering medication to rooms." 
    @Override
    public void performDuty() {
        System.out.println("Robot " + staffId + " is delivering medication to rooms.");
    }

    // performSanitization(): Print "Robot is undergoing a UV-light sterilization process." 
    @Override
    public void performSanitization() {
        System.out.println("Robot is undergoing a UV-light sterilization process.");
    }
}
