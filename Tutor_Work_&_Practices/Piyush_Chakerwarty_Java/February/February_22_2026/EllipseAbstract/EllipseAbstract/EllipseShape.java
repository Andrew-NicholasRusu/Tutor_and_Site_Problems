package EllipseAbstract.EllipseAbstract;

public abstract class EllipseShape {
    protected double x, y; // center / position

    // Constructor
    public EllipseShape (double x, double y) {
        this.x = x;
        this.y = y;
    }

    // Methods
    public abstract void draw();

    public abstract double area();
}
