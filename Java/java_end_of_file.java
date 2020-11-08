import java.util.*;

public class java_end_of_file {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = 1;
		while (sc.hasNext()) {
			String s = sc.nextLine();
			System.out.println(n++ + " " + s);
		}
	}
}
