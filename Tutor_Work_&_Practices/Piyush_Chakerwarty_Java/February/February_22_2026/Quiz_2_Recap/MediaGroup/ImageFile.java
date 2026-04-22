package Quiz_2_Recap.MediaGroup;

public class ImageFile extends MediaFile {
    // Attributes
    private String dimensions;

    // No-argument Constructor
    public ImageFile() {
        super();
        this.dimensions = "";
    }

    // Constructor
    public ImageFile (String fileName, double fileSize, String dimensions) {
        super (fileName, fileSize);
        this.dimensions = dimensions;
    }

    public String getDimensions() {
        return dimensions;
    }

    public void setDimensions(String dimensions) {
        this.dimensions = dimensions;
    }

    @Override
    public void open() {
        System.out.printf("Displaying image: %s (Dimensions: %s). \n",
                this.getFileName(), this.getDimensions());
    }
}
