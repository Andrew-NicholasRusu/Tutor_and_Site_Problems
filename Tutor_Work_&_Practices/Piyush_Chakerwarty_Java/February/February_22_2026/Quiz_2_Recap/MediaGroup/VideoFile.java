package Quiz_2_Recap.MediaGroup;

public class VideoFile extends MediaFile {
    /*
    Attributes
    // int duration - duration in seconds
    // String resolution - video resolution (e.g., "1920x1080").
    */
    private int duration;
    private String resolution;

    // No-argument Constructor
    public VideoFile() {
        super();
        this.duration = 0;
        this.resolution = "";
    }

    // Constructor
    public VideoFile (String fileName, double fileSize, int duration, String resolution) {
        super (fileName, fileSize);
        this.duration = duration;
        this.resolution = resolution;
    }

    // Getters and Setters
    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }

    public String getResolution() {
        return resolution;
    }

    public void setResolution(String resolution) {
        this.resolution = resolution;
    }

    // Method
    @Override
    public void open() {
        // Playing audio file: [fileName] (Duration: [duration] seconds)."
        System.out.printf("Playing video file: %s (Duration: [%d] seconds).\n",
                this.getFileName(), this.getResolution(), this.getDuration());
    }
}
