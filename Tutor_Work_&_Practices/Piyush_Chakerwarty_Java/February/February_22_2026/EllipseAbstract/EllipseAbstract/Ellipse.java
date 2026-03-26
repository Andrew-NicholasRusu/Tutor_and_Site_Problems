package EllipseAbstract.EllipseAbstract;

public class Ellipse extends EllipseShape {
    // Attributes
    private double rx;
    private double ry;
    // radii along x and y

    // Constructor
    public Ellipse (double x, double y, double rx, double ry) {
        super (x, y);
        this.rx = rx;
        this.ry = ry;
    }

    @Override
    public void draw() {
        // placeholder rendering
        System.out.printf("Ellipse at (%.2f, %.2f) rx=%.2f ry=%.2f%n", x, y, rx, ry);
    }

    @Override
    public double area() {
        return Math.PI * rx * ry;
    }
}
