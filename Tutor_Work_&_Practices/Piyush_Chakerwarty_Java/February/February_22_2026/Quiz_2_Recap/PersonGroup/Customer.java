package Quiz_2_Recap.PersonGroup;

public class Customer extends Person {
    private String customerNumber;
    private boolean mailingList;

    // NO-ARGUMENT CONSTRUCTOR
    public Customer () {
        super ();
        this.customerNumber = "";
        this.mailingList = isMailingList();

    }

    // CONSTRUCTOR
    public Customer (String name, String address, String phone,
                     String customerNumber, boolean mailingList){
        super (name, address, phone);
        this.customerNumber = customerNumber;
        this.mailingList = mailingList;
    }

    // GETTERS AND SETTERS
    public String getCustomerNumber() {
        return customerNumber;
    }

    public void setCustomerNumber(String customerNumber) {
        this.customerNumber = customerNumber;
    }

    public boolean isMailingList() {
        return mailingList;
    }

    public void setMailingList(boolean mailingList) {
        this.mailingList = mailingList;
    }

    // OVERRIDE TO-STRING METHOD
    @Override
    public String toString() {
        return "Name: " + getName() + "\nAddress: " + getAddress() + "\nTelephone: " + getPhone() +
                "\nCustomer Number: " + getCustomerNumber() + "\nMailing List: " + isMailingList();
    }
}
