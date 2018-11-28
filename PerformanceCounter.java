import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class PerformanceCounter {


    public static void main(String[] args) throws FileNotFoundException {
                                    //      ^yes i know that's bad but idgaf


        float total = 8793;
        float DNAcount = 0;
        float RNAcount = 0;
        float DRNAcount = 0;
        float NONDRNAcount = 0;

        File input = new File("tsttrain2.csv");
        Scanner scan = new Scanner(input);

        scan.nextLine();

        while(scan.hasNextLine())
        {

            String line = scan.nextLine();
            String[] features = line.split("\\,");

            int length = features.length;

            String prediction = features[length - 1];
            prediction = prediction.substring(1, prediction.length() - 1);
            System.out.println(prediction);


            if (prediction.equals("nonDRNA"))
            {
                NONDRNAcount++;
            }
            else if(prediction.equals("DNA"))
            {
                DNAcount++;
            }
            else if(prediction.equals("DRNA"))
            {
                DRNAcount++;
            }
            else if(prediction.equals("RNA"))
            {
                RNAcount++;
            }
        }

        System.out.println();
        System.out.println();
        System.out.println("Report:");


        float DNAperc = (DNAcount/total) * 100;
        float RNAperc = (RNAcount/total) * 100;
        float DRNAperc = (DRNAcount/total) * 100;
        float NONDRNAperc = (NONDRNAcount/total) * 100;

        System.out.println("=============================================================================================");
        System.out.println("DNA:     " + DNAcount + "   " + DNAperc + "%");
        System.out.println("RNA:     " + RNAcount +  "   " + RNAperc + "%");
        System.out.println("DRNA:    " + DRNAcount +  "     " + DRNAperc + "%");
        System.out.println("nonDRNA: " + NONDRNAcount +  "  " + NONDRNAperc + "%");
        System.out.println("=============================================================================================");

    }

}
