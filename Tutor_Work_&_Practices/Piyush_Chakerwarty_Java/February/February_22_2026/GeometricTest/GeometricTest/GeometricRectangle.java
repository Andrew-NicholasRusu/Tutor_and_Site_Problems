package GeometricTest.GeometricTest;
public class GeometricRectangle extends GeometricObject {
    private double width;
    private double length;

    public GeometricRectangle(String color, boolean filled, double width, double length) {
        super (color, filled);
        this.width = width;
        this.length = length;
    }

    public double getWidth() {
        return width;
    }

    public void setWidth(double width) {
        this.width = width;
    }

    public double getLength() {
        return length;
    }

    public void setLength(double length) {
        this.length = length;
    }

    @Override
    public String toString() {
        return "{" + super.toString() + ", width: " + this.width + ", length: " + this.length + "}";
    }

    @Override
    public boolean equals(Object otherObject) {
        if (!(otherObject instanceof GeometricRectangle)) {
            return false;
        }

        GeometricRectangle otherGeometricRectangle = (GeometricRectangle) otherObject;
        return this.width == otherGeometricRectangle.width && 
               this.length == otherGeometricRectangle.length && 
               super.equals(otherGeometricRectangle);
    }
}