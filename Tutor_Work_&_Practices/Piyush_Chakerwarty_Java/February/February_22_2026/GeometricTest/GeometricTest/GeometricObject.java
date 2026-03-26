package GeometricTest.GeometricTest;

public class GeometricObject {
    private String color;
    private boolean filled;

    public GeometricObject(String color, boolean filled) {
        this.color = color;
        this.filled = filled;
    }

    public String getColor() {
        return color;
    }

    public boolean isFilled() {
        return filled;
    }

    @Override
    public String toString() {
        return "Color: " + this.color + ", filled: " + this.filled;
    }

    public boolean equals(Object otherObject) {
        if(!(otherObject instanceof GeometricObject)) {
            return false;
        }
        GeometricObject otherGeometricObject = (GeometricObject) otherObject;
        if (this.color == otherGeometricObject.color && this.filled == otherGeometricObject.filled) {
            return true;
        } else {
            return false;
        }
    }
}
