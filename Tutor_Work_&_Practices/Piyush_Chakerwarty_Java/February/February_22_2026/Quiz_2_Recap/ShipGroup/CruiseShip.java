package Quiz_2_Recap.ShipGroup;

public class CruiseShip extends Ship {
    // ATTRIBUTE
    private String maxPassengers;

    // NO-ARGUMENT CONSTRUCTOR
    public CruiseShip() {
        super();
        this.maxPassengers = "";
    }

    // CONSTRUCTOR
    public CruiseShip (String name, String maxPassengers) {
        super (name, "");
    }

    // GETTER AND SETTER

    public String getMaxPassengers() {
        return maxPassengers;
    }

    public void setMaxPassengers(String maxPassengers) {
        this.maxPassengers = maxPassengers;
    }

    // OVERRIDE TO-STRING
    @Override
    public String toString(){
        return "Name: " + getName() + "\nMaximum passengers: " + getMaxPassengers();
    }
}
