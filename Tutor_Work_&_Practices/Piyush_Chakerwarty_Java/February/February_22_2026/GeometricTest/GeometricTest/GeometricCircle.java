package GeometricTest.GeometricTest;

public class GeometricCircle extends GeometricObject {
    private double radius;

    public GeometricCircle (String color, boolean filled, double radius) {
        super(color, filled);
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    @Override
    public String toString() {
        return "{" + super.toString() + ", radius: " + this.radius + "}";
    }

    @Override
    public boolean equals(Object otherObject) {
        if (!(otherObject instanceof GeometricCircle)) {
            return false;
        }

        GeometricCircle otherGeometricCircle = (GeometricCircle) otherObject;
        if (this.radius == otherGeometricCircle.radius && super.equals(otherGeometricCircle)) {
            return true;
        } else {
            return false;
        }
    }
}
