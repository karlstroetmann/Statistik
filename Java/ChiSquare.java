import java.util.*;
import java.util.regex.*;
import java.io.*;
import java.lang.Math.*;

public class ChiSquare 
{
    private ArrayList<Date> mDeathDates;
    private Integer[]       mWeekDays;
    private Integer         mTotal;
    private Double          mChiSquare;

    public static void main(String[] args) {
        ChiSquare chi2 = new ChiSquare("cemetery.txt");
    }
        
    public ChiSquare(String fileName) {
        mDeathDates = new ArrayList<Date>();
        mWeekDays   = new Integer[7];
        for (int i = 0; i < 7; ++i) {
            mWeekDays[i] = 0;
        }
        try {
            FileReader     fr   = new FileReader(fileName);
            BufferedReader br   = new BufferedReader(fr);
            String         line = br.readLine();
            while (line != null) {
                try {
                    Pattern  whiteSpace = Pattern.compile("[ \t]+");
                    String[] tokenArray = whiteSpace.split(line);
                    String   date       = tokenArray[tokenArray.length-1];
                    Pattern  slash      = Pattern.compile("[/]");
                    String[] dayMonYear = slash.split(date);
                    Integer  day        = Integer.parseInt(dayMonYear[0]);
                    Integer  month      = Integer.parseInt(dayMonYear[1]);
                    Integer  year       = Integer.parseInt(dayMonYear[2]);
                    mDeathDates.add(new Date(year - 1900, month - 1, day));
                } catch (IllegalArgumentException ae) {}
                line = br.readLine();
            }
        } catch  (FileNotFoundException fe) {
            System.out.println("File \"" + fileName + "\" not found!");
            System.exit(2);
        } catch (IOException e) {
            System.out.println("IOException reading from \"" + fileName +"\"!");
            System.exit(3);
        } 
        for (Date date: mDeathDates) {
            int day = date.getDay();
            ++mWeekDays[day];
        }
        mTotal = 0;
        for (int i = 0; i < 7; ++i) {
            mTotal += mWeekDays[i];
            System.out.println(i + ":  " + mWeekDays[i]);
        }
        System.out.println("Total: " + mTotal);
        mChiSquare = 0.0;
        double seventhPart = mTotal / 7.0;
        for (int k = 0; k < 7; ++k) {
            mChiSquare += (mWeekDays[k] - seventhPart)*(mWeekDays[k] - seventhPart)/seventhPart;
        }
        double probabilty = Math.exp(-mChiSquare/2) * (1.0 + (0.5 + 0.125*mChiSquare) * mChiSquare);
        System.out.println("ChiSquare   = " + mChiSquare);
        System.out.println("Probability = " + probabilty);
    }
}
