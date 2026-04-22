package Quiz_2_Recap.ShipGroup;

public class Ship {
    // ATTRIBUTES
    private String name;
    private String year;

    // NO-ARGUMENT CONSTRUCTOR
    public Ship() {
        this.name = "";
        this.year = "";
    }

    // CONSTRUCTOR
    public Ship (String name, String year) {
        this.name = name;
        this.year = year;
    }

    // GETTERS AND SETTERS
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }

    // TO-STRING
    public String toString(){
        return "Name: " + getName() + "\nYear built: " + getYear();
    }
}
