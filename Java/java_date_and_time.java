import java.io.*;
import java.math.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;

class Result {
	static String WEEK_DAY[] = {"SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"};
	
    public static String findDay(int month, int day, int year) {
    	Calendar cal = Calendar.getInstance();
    	cal.set(year, month-1, day);
    	return WEEK_DAY[cal.get(Calendar.DAY_OF_WEEK) - 1];
    }
}

public class java_date_and_time {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int month = sc.nextInt();
        int day = sc.nextInt();
        int year = sc.nextInt();
        System.out.println(Result.findDay(month, day, year));
    }
}
