import java.util.*;

public class java_string_reverse {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		int len = s.length();
		for (int i = 0, j = len-1; i < j; i++, j--) {
			if (s.charAt(i) != s.charAt(j)) {
				System.out.println("No");
				System.exit(0);
			}
		}
		System.out.println("Yes");
	}
}
