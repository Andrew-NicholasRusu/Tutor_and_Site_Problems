package BirdGroup;

public class Penguin extends Bird implements GroundBird {

    // Constructor that inherits the abstract class
    public Penguin (String color, String species, boolean canFly, String gender) {
        super(color, species, canFly, gender);
    }
    
    // Overriding the methods
    @Override
    public void canLayEggs() {
        System.out.println("This bird can lay eggs.");
    }

    @Override
    public void eat() {
        System.out.println("This bird preferably eats fish by swallowing their food whole.");
    }

    // Interface methods
    @Override
    public void walk() {
        System.out.println("The " + getSpecies() + " walk with a distinct, side-to-side waddle on land.");
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
