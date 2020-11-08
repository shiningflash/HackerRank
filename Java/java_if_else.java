import java.util.Scanner;

public class java_if_else {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		if (n % 2 == 1) System.out.println("Weird");
		else System.out.println((n >= 6 && n <= 20) ? "Weird" : "Not Weird");
		sc.close();
	}
}
