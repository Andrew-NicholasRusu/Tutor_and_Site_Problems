package Quiz_2_Recap.MediaGroup;

public class AudioFile extends MediaFile {

    // Additional attribute: int duration - duration in seconds
    private int duration;

    // Constructors
    public AudioFile() {
        super ();
        this.duration = 0;
    }

    public AudioFile(String fileName, double fileSize, int duration) {
        super (fileName, fileSize);
        this.duration = duration;
    }

    // Getters and Setters
    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }

    // Method
    @Override
    public void open() {
        // Playing audio file: [fileName] (Duration: [duration] seconds)."
        System.out.printf("Playing audio file: %s (Duration: [%d] seconds).\n",
                this.getFileName(), this.getDuration());

    }
}
