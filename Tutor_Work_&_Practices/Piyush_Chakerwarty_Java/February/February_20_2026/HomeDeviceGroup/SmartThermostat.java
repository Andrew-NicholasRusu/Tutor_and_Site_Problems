package HomeDeviceGroup;

public class SmartThermostat extends HomeDevice implements RemoteControllable {

    // New Attribute: private int temperature. 
    private int temperature;

    // Constructor
    public SmartThermostat (String deviceName, boolean isConnected, int temperature) {
        super (deviceName, isConnected);
        this.temperature = temperature;
    }

    public int getTemperature() {
        return temperature;
    }

    public void setTemperature(int temperature) {
        this.temperature = temperature;
    }

    @Override
    public void performAction() {
        System.out.println("Adjusting climate to " + temperature + " degrees.");
    }

    @Override
    public void connectToWifi() {
        this.isConnected = true;
        System.out.println("Thermostat linked to cloud.");
    }

    @Override
    public int signalStrength() {
        return 3;
    }
}