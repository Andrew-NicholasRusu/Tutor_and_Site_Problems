package PolymorphismTest;

public class CirclePolymorphism extends ShapePolymorphism {
    private double radius;

    public CirclePolymorphism (String color, double radius) {
        super (color);
        this.radius = radius;
    }

    // Methods
    @Override 
    double getArea() {
        return Math.PI * this.radius * this.radius;
    }

    @Override
    double getPerimeter() {
        return 2 * Math.PI * this.radius;
    }

}
