package PolymorphismTest;

public class TrianglePolymorphism extends ShapePolymorphism {
    // Attributes:
    private double side1;
    private double side2;
    private double side3;

    // Constructor
    public TrianglePolymorphism (String color, double side1, double side2, double side3) {
        super (color);
        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;
    }

    @Override
    double getArea() {
        // Using Heron's formula
        double s = getPerimeter() / 2;
        return Math.sqrt(s *(s - this.side1)*(s - this.side2)*(s - this.side3));
    }

    @Override
    double getPerimeter() {
        return this.side1 + this.side2 + this.side3;
    }
}
