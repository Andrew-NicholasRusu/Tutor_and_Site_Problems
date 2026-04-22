package BirdGroup;

public class Eagle extends Bird {

    public Eagle (String color, String species, boolean canFly, String gender) {
        super(color, species, canFly, gender);
    }

    // Methods 
    @Override
    public void canLayEggs() {
        System.out.println("The " + getSpecies() + " lays their eggs in high-up re-used stick nests.");
    }

    @Override
    public void eat() {
        System.out.println("The " + getSpecies() + " use their sharp, hooked beaks and talons to eat their prey.");
    }

    @Override
    public String toString() {
        return "Color: " + getColor() + ", Species: " + getSpecies() + ", Can it Fly? " + getCanFly() + ", Gender: " + getGender();
    }
}

