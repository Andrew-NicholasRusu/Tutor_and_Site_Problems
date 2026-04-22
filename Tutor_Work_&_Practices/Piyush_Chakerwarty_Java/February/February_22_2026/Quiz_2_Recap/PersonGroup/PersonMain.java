package Quiz_2_Recap.PersonGroup;

public class PersonMain {
    public static void main(String[] args) {
        Customer customer1 = new Customer("Julie James", "123 Main Street",
                "555-1212", "147-A049", true);

        Customer customer2 = new Customer("Joan Jones", "123 Main Street",
                "514-6130", "147-A099", false);

        PreferredCustomer preferredCustomer1 = new PreferredCustomer("Julie James", "123 Main Street",
                "555-1212", "147-A049", true, 1750.00, 0.07);

        PreferredCustomer preferredCustomer2 = new PreferredCustomer("Joan Jones", "123 Main Street",
                "514-6130", "147-A099", false, 3009.00, 0.19);

        System.out.println("Here's the first customer.");
        System.out.println(customer1);
        System.out.println();

        System.out.println("Here's the second customer.");
        System.out.println(customer2);
        System.out.println();

        System.out.println("Here's the first preferred customer:");
        System.out.println(preferredCustomer1);
        System.out.println();

        System.out.println("Here's the second preferred customer:");
        System.out.println(preferredCustomer2);
        System.out.println();
    }
}
