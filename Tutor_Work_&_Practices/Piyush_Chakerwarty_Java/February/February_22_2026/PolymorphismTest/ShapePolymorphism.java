package PolymorphismTest;

public abstract class ShapePolymorphism {
    protected String color;

    public ShapePolymorphism(String color) {
        this.color = color;
    }

    // Abstract methods - must be implemented by subclasses.
    abstract double getArea();
    abstract double getPerimeter();

    // Concrete method - shared by all shapes
    public void displayInfo() {
        System.out.println("Shape: " + this.getClass().getSimpleName());
        System.out.println("Color: " + this.color);
        System.out.println("Area: " + getArea());
        System.out.println("Perimeter: " + getPerimeter());
    }
}
