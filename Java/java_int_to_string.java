import java.util.Scanner;

public class java_int_to_string {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		try {
			String n = String.valueOf(sc.nextInt());
			System.out.println("Good job");
		}
		catch(Exception e) {
			System.out.println( "Wrong answer");
		}
	}
}
