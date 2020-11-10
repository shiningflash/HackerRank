import java.util.*;

public class java_arraylist {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList<ArrayList<Integer>> list = new ArrayList<ArrayList<Integer>>();
		int n = sc.nextInt();
		for (int i = 0; i < n; i++) {
			list.add(new ArrayList<Integer>());
			int x = sc.nextInt();
			for (int j = 0; j < x; j++) {
				int m = sc.nextInt();
				list.get(i).add(m);
			}
		}
		int q = sc.nextInt();
		for (int i = 0; i < q; i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			try {
				System.out.println(list.get(x-1).get(y-1));
			} catch(Exception e) {
				System.out.println("ERROR!");
			}
		}
	}
}
