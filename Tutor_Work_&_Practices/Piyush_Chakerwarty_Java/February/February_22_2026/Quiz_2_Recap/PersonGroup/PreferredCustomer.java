package Quiz_2_Recap.PersonGroup;

// Design a class named PreferredCustomer, which
// inherits from the Customer class you created in previous
// problem. The PreferredCustomer class should have
// fields for
// the amount of the customer’s purchases and
// the customer’s discount level.

public class PreferredCustomer extends Customer {
    // ATTRIBUTES
    private double purchases;
    private double discountLevel;

    // Write one or more constructors and the appropriate
    // mutator and accessor methods for the class’s fields

    // NO-ARGUMENT CONSTRUCTOR
    public PreferredCustomer() {
        super();
        this.purchases = 0.0;
        this.discountLevel = 0.0;
    }

    // CONSTRUCTOR
    public PreferredCustomer(String name, String address, String phone, String customerNumber,
                             boolean mailingList, double purchases, double discountLevel){
        super(customerNumber, phone, customerNumber, address, mailingList);
        this.purchases = purchases;
        this.discountLevel = discountLevel;
    }

    // GETTERS AND SETTERS
    public double getDiscountLevel() {
        // When a preferred customer spends $500, he or she
            // gets a 5 percent discount on all future purchases.
        // When a preferred customer spends $1,000, he or she
            // gets a 6 percent discount on all future purchases.
        // When a preferred customer spends $1,500, he or she
            //gets a 7 percent discount on all future purchases.
        // When a preferred customer spends $2,000 or more,
            // he or she gets a 10 percent discount on all future purchases.
        if (getPurchases() <= 500) {
            discountLevel = 0.05;
        } else if (getPurchases() <= 1000) {
            discountLevel = 0.06;
        } else if (getPurchases() <= 1500) {
            discountLevel = 0.07;
        } else if (getPurchases() <= 2000) {
            discountLevel = 0.1;
        }
        return discountLevel;
    }

    public void setDiscountLevel(double discountLevel) {
        this.discountLevel = discountLevel;
    }

    public double getPurchases() {
        return purchases;
    }

    public void setPurchases(double purchases) {
        this.purchases = purchases;
    }

    // OVERRIDE TO-STRING METHOD
    @Override
    public String toString() {
        return "Name: " + getName() + "\nAddress: " + getAddress() + "\nTelephone: " + getPhone() +
                "\nCustomer Number: " + getCustomerNumber() + "\nMailing List: " + isMailingList() +
                "\nPurchases: " + getPurchases() + "\nDiscount Level: " + getDiscountLevel();
    }
}
