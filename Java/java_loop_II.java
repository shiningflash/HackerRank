import java.util.*;

public class java_loop_II {
	static Scanner sc = new Scanner(System.in);
	
	public static void solve() {
		int a = sc.nextInt();
		int b = sc.nextInt();
		int n = sc.nextInt();
		long sum = a;
		for (int i = 0; i < n; i++) {
			sum += Math.pow(2, i) * b;
			System.out.print(sum + (i == n-1 ? "\n" : " "));
		}
	}
	
	public static void main(String[] args) {
		int q = sc.nextInt();
		for (int i = 0; i < q; i++) solve();
	}
}
