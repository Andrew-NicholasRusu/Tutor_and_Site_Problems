package Quiz_2_Recap.MediaGroup;
import java.util.ArrayList;

public class MediaMain {
    public static void main(String[] args) {


        ArrayList<MediaFile> mediaFiles = new ArrayList<>();
        //  Sample output:
        //  Playing audio file: LifeOfaProgrammer.mp3 (Duration: 240 seconds).
        //  Playing video file: DebuggingTheMatrix.mp4 (Resolution: 1920x1080, Duration: 7200 seconds).
        //  Displaying image: 404_Image_Not_Found.jpg (Dimensions: 1024x768).
        //  Playing audio file: Polymorphin_Aint_Easy.mp3 (Duration: 240 seconds).

        AudioFile audioFile = new AudioFile("LifeOfaProgrammer.mp3", 10, 240);
        VideoFile videoFile = new VideoFile("DebuggingTheMatrix.mp4", 20, 7200, "1920x1080");
        ImageFile imageFile = new ImageFile("404_Image_Not_Found.jpg", 15, "1024x768");
        AudioFile audioFile2 = new AudioFile("Polymorphism_Ain't_Easy.mp3", 5, 240);

        mediaFiles.add(audioFile);
        mediaFiles.add(videoFile);
        mediaFiles.add(imageFile);
        mediaFiles.add(audioFile2);

        // Use a loop to iterate over the list, and for each media file, call its open() method.
        for (int i = 0; i < mediaFiles.size(); i++) {
            MediaFile mediaFile = mediaFiles.get(i);
            System.out.println(mediaFile);
        }
    }
}
