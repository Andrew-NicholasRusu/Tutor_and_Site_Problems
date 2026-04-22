package Quiz_2_Recap.MediaGroup;

public abstract class MediaFile {
    // Attributes
    private String fileName;
    private double fileSize;

    // Constructors
    public MediaFile() {
        this.fileName = "";
        this.fileSize = 0;
    }

    public MediaFile(String fileName, double fileSize) {
        this.fileName = fileName;
        this.fileSize = fileSize;
    }

    // Getters and Setters
    public String getFileName() {
        return fileName;
    }

    public void setFileName(String fileName) {
        this.fileName = fileName;
    }

    public double getFileSize() {
        return fileSize;
    }

    public void setFileSize(double fileSize) {
        this.fileSize = fileSize;
    }

    // Method
    public abstract void open();
}
