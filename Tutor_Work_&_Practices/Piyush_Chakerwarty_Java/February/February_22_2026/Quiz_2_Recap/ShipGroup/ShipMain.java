package Quiz_2_Recap.ShipGroup;

public class ShipMain {

    // Demonstrate the classes in a program that has a Ship array. Assign various Ship, CruiseShip, and CargoShip
    // objects to the array elements. The program should then step through the array, calling each object’s
    // toString method.
    public static void main(String[] args) {

        // ARRAY
        Ship[] shipStorage = new Ship[3];

        // OBJECTS
        Ship ship1 = new Ship("Lollipop", "1960");
        CruiseShip ship2 = new CruiseShip("Disney Magic", "2400");
        CargoShip ship3 = new CargoShip("Black Pearl", "50000");

        shipStorage[0] = ship1;
        shipStorage[1] = ship2;
        shipStorage[2] = ship3;

        // POLYMORPHIC method calls
        for (Ship ship : shipStorage) {
            System.out.println(ship.toString());
        }
    }
}
