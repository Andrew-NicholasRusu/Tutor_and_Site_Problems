package PolymorphismTest;

public class EllipsePolymorphism extends ShapePolymorphism {
    private double majorAxis;
    private double minorAxis;

    public EllipsePolymorphism (String color, double majorAxis, double minorAxis) {
        super (color);
        this.majorAxis = majorAxis;
        this.minorAxis = minorAxis;
    }

    @Override
    double getArea() {
        return Math.PI * this.majorAxis * this.minorAxis;
    }

    @Override
    double getPerimeter() {
        // Approximation formula
        return Math.PI * (3 * (this.majorAxis * this.minorAxis) -
        Math.sqrt((3 * this.majorAxis + this.minorAxis) * (this.majorAxis + 3 * this.minorAxis)));
    }
}
