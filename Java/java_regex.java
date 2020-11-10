import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Scanner;

class MyRegex {
	static String ip = "([01]?\\d{1,2}|2[0-4]\\d|25[0-5])";
	static String pattern = ip + "." + ip + "." + ip + "." + ip;
}

class java_regex{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        while(in.hasNext()){
            String IP = in.next();
            System.out.println(IP.matches(new MyRegex().pattern));
        }
    }
}