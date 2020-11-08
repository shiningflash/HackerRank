import java.util.Scanner;

public class java_stdin_and_stdout_1 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for (int i = 0; i < 3; i++) {
			int n = sc.nextInt();
			System.out.println(n);
		}
		sc.close();
	}
}
