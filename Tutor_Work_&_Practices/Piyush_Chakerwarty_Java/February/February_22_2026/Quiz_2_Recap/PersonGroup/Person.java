package Quiz_2_Recap.PersonGroup;

public class Person {
    private String name;
    private String address;
    private String phone;

    // NO-ARGUMENT CONSTRUCTOR
    public Person () {
        this.name = "";
        this.address = "";
        this.phone = "";
    }

    // ALL-ARGUMENT CONSTRUCTOR
    public Person (String name, String address, String phone) {
        this.name = name;
        this.address = address;
        this.phone = phone;
    }

    // GETTERS AND SETTERS
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
