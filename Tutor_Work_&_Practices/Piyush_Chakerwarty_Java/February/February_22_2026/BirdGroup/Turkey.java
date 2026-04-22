package BirdGroup;

public class Turkey extends Bird implements GroundBird {

    public Turkey (String color, String species, boolean canFly, String gender) {
        super(color, species, canFly, gender);
    }

    // Methods
    @Override
    public void canLayEggs() {
        System.out.println("This bird can lay eggs.");
    }

    @Override
    public void eat() {
        System.out.println("This bird preferably eats a varied diet of seeds, nuts, berries, insects, worms, etc.");
    }

    // Interface methods
    @Override
    public void walk() {
        System.out.println("The " + getSpecies() + " walk with a distinct, slow, and wide-stanced gait.");
    }

    @Override
    public void groundNest() {
        System.out.println("The " + getSpecies() + " has a ground nest to lay their eggs before they hatch.");
    }

    @Override
    public String toString() {
        return "Color: " + getColor() + ", Species: " + getSpecies() + ", Can it Fly? " + getCanFly() + ", Gender: " + getGender();
    }
}
