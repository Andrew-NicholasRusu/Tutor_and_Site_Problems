package BirdGroup;

public abstract class Bird {
    // Attributes
    private String color;
    private String species;
    private boolean canFly;
    private String gender;

    // Constructor
    public Bird (String color, String species, boolean canFly, String gender) {
        this.color = color;
        this.species = species;
        this.canFly = canFly;
        this.gender = gender;
    }

    // Getters and Setters
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String getSpecies() {
        return species;
    }

    public void setSpecies(String species) {
        this.species = species;
    }

    public boolean getCanFly() {
        return canFly;
    }

    public void setCanFly(boolean canFly) {
        this.canFly = canFly;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    
    // Abstract methods
    // Will be used in subclasses
    public abstract void canLayEggs();

    public abstract void eat();
}