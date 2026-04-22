package Quiz_2_Recap.PolyClassGroup;

import java.util.ArrayList;

public class Overriding_Example {
    public static void main(String[] args) {
        // Create an ArrayList
        ArrayList<PolyClass> list = new ArrayList<>();
        PolyClass polyClass1 = new PolyClass();
        list.add(polyClass1);
        PolyClass polyClass3 = new PolyClassExtension();
        list.add(polyClass3);
        PolyClassExtension polyClass4 = new PolyClassSubClassExtension();
        list.add(1, polyClass4);
        PolyClassExtension polyClass5 = new PolyClassSubClassExtension();
        list.add(polyClass5);
        list.add(2, new PolyClassSubClassExtension());
        list.add(polyClass3);
        list.remove(3);
        PolyClass polyClass6 = polyClass1;
        list.set(3, polyClass6);

        // For each object, call methods x(), s(), y(), and z()
        for (PolyClass obj : list) {
            System.out.println("Testing object of type: " +
                    obj.getClass().getSimpleName());
            obj.x();
            obj.s();
            obj.y();
            obj.z();
            System.out.println();
        }
    }
}
