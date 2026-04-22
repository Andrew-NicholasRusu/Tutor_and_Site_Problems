package PolymorphismTest;

public class RectanglePolymorphism extends ShapePolymorphism {
    // Attributes
    private final double width;
    private final double height;

    // Constructor
    public RectanglePolymorphism (String color, double width, double height) {
        super (color);
        this.width = width;
        this.height = height;
    }

    // Override methods from Shape
    @Override
    double getArea() {
        return this.width * this.height;
    }

    @Override
    double getPerimeter() {
        return 2 * (this.width + this.height);
    }
}
