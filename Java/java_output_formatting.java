import java.util.Scanner;

public class java_output_formatting {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("================================");
		while (sc.hasNext()) {
			String s = sc.next();
			int n = sc.nextInt();
			System.out.print(s);
			for (int i = s.length(); i < 15; i++)
				System.out.print(' ');
			if (n < 10) System.out.print("00");
			else if (n < 100) System.out.print("0");
			System.out.println(n);
		}
		System.out.println("================================");
	}
}
