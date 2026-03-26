package GeometricTest.GeometricTest;

public class GeometricMain {
    public static void main(String[] args) {
        GeometricObject go = new GeometricObject("Red", true);
        System.out.println(go);

        GeometricCircle circle1 = new GeometricCircle("Blue", false, 5);
        System.out.println(circle1);

        GeometricCircle circle2 = new GeometricCircle("Blue", false, 5);
        System.out.println(circle2);

        GeometricRectangle rectangle1 = new GeometricRectangle("Green", true, 8, 9);
        System.out.println(rectangle1);

        GeometricRectangle rectangle2 = new GeometricRectangle("Purple", true, 6, 7);
        System.out.println(rectangle2);

        System.out.println("circle1 == circle2? " + circle1.equals(circle2)); // true
        System.out.println("rectangle1 == rectangle2? " + rectangle1.equals(rectangle2)); // false
    }

}
