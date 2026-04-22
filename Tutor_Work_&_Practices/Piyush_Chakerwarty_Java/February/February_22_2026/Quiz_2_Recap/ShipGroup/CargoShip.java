package Quiz_2_Recap.ShipGroup;

public class CargoShip extends Ship {
    // ATTRIBUTE
    private String cargoCapacity;

    // NO-ARGUMENT CONSTRUCTOR
    public CargoShip () {
        super();
        this.cargoCapacity = "";
    }

    // CONSTRUCTOR
    public CargoShip (String name, String cargoCapacity) {
        super(name, "");
        this.cargoCapacity = cargoCapacity;
    }

    // GETTER AND SETTER
    public String getCargoCapacity() {
        return cargoCapacity;
    }

    public void setCargoCapacity(String cargoCapacity) {
        this.cargoCapacity = cargoCapacity;
    }

    // OVERRIDE TO-STRING
    @Override
    public String toString() {
        return "Name: " + getName() + "\nCargo Capacity: " + getCargoCapacity() + " tons";
    }
}