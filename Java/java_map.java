import java.util.HashMap;
import java.util.Scanner;

public class java_map {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		HashMap<String, Integer> map = new HashMap<>();
		for (int i = 0; i < n; i++) {
			sc.nextLine();
			String s = sc.nextLine();
			int x = sc.nextInt();
			map.put(s, x);
		}
		sc.nextLine();
		while (sc.hasNext()) {
			String s = sc.nextLine();
			if (map.get(s) == null) System.out.println("Not found");
			else System.out.printf("%s=%d\n", s, map.get(s));
		}
	}
}
