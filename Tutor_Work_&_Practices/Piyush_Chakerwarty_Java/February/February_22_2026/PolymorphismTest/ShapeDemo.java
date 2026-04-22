package PolymorphismTest;

public class ShapeDemo {
    public static void main(String[] args) {
        // Polymorphic array - all elements are Shape references
        ShapePolymorphism[] shapes = new ShapePolymorphism[5];

        shapes[0] = new RectanglePolymorphism("Red", 5, 10);
        shapes[1] = new SquarePolymorphism("Blue", 4);
        shapes[2] = new CirclePolymorphism("Green", 3);
        shapes[3] = new EllipsePolymorphism("Yellow", 5, 3);
        shapes[4] = new TrianglePolymorphism("Purple", 3, 4, 5);

        // REFRESH CANVAS: One loop to rule them all.
        for (ShapePolymorphism s : shapes) { // Nested loop
            double area = s.getArea(); // Runtime Polymorphism: calls the correct version!
            System.out.println("Area is: " + area);
        }
        // Another Polymorphic method calls
        for (ShapePolymorphism shape : shapes) {
            shape.displayInfo(); // the output of this method depends on the object type
        }
    }
}
