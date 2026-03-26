package HomeDeviceGroup;

// Abstract class
public abstract class HomeDevice {
    // Attributes: protected String deviceName and protected boolean isConnected.
    protected String deviceName;
    protected boolean isConnected;

    // Constructor: Initializes the name and sets isConnected to false. 
    public HomeDevice (String deviceName, boolean isConnected) {
        this.deviceName = deviceName;
        this.isConnected = false;
    }

    // Abstract Method: public abstract void performAction(). 
    public abstract void performAction();

    // Concrete Method: public void showStatus() which prints if the device is currently connected. 
    public void showStatus() {
        System.out.println(" The device is connected? " + isConnected);
    }



}
