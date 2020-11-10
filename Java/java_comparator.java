import java.util.*;

public class java_comparator {
	public static class PlayerComparator implements Comparator<Player> {
		@Override
		public int compare(Player p1, Player p2) {
			if (p1.score != p2.score) return p2.score - p1.score;
			return p1.name.compareTo(p2.name);
		}
	}
	
	public static class Player {
		String name;
		int score;
		
		Player(String name, int score) {
			this.name = name;
			this.score = score;
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		List<Player> list = new ArrayList<Player>();
		for (int i = 0; i < n; i++) {
			String name = sc.next();
			int score = sc.nextInt();
			list.add(new Player(name, score));
		}
		Collections.sort(list, new PlayerComparator());
		for (Player p: list) System.out.println(p.name + " " + p.score);
	}
}
