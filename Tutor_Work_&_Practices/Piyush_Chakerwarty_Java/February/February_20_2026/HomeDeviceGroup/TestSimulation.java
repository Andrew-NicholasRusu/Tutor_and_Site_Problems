package HomeDeviceGroup;

public class TestSimulation {
    public static void main(String[] args) {
        // In your main method, create an array of HomeDevice containing one of each. 
        SmartBulb test1 = new SmartBulb("Philips Hue", false);
        SmartThermostat test2 = new SmartThermostat("Google Nest", true, 26);

        // Array named devices
        HomeDevice[] devices = new HomeDevice[2]; // 2 objects
        devices[0] = test1; // index 0
        devices[1] = test2;  // index 1

        // Write a loop to perform the following Test Run: 
        for (int i = 0; i < devices.length; i++) {
            devices[i].performAction();
            // Dynamic Interface Check: 
                // Check if the device is an instanceof RemoteControllable. 
                // If it is, cast it and call connectToWifi(). 
            if (devices[i] instanceof RemoteControllable) {
               ((RemoteControllable)devices[i]).connectToWifi();
            }
        }
        // Final Report: Call showStatus() for both devices to confirm the connection worked. 
        test1.showStatus();
        test2.showStatus();
        
    }
}
