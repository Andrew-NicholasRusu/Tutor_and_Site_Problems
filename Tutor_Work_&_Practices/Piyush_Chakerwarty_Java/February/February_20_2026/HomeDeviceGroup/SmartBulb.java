package HomeDeviceGroup;

// Inheritance: Extends HomeDevice and implements RemoteControllable. 
public class SmartBulb extends HomeDevice implements RemoteControllable {

    public SmartBulb(String deviceName, boolean isConnected) {
        super(deviceName, isConnected);
    }

    @Override
    public void performAction(){
    // performAction(): Prints "The bulb is shining at 100% brightness." 
        System.out.println("The bulb is shinning at 100% brightness");
    }

    @Override
    // connectToWifi(): Sets isConnected to true and prints "Bulb joined the network." 
    public void connectToWifi(){
        this.isConnected = true;
        System.out.println("Bulb joined the network.");
    }

    @Override
    // signalStrength(): Returns a fixed value of 4. 
    public int signalStrength() {
        return 4;
    }

}
