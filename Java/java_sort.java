import java.util.*;

public class java_sort {
	public static class StudentComparator implements Comparator<Student> {
		@Override
		public int compare(Student s1, Student s2) {
			if ((int)(s1.cgpa*1000) != (int)(s2.cgpa*1000)) return ((int)(s2.cgpa*1000) - (int)(s1.cgpa*1000));
			if (!s1.name.equals(s2.name)) return s1.name.compareTo(s2.name);
			return s1.id - s2.id;
		}
	}
	
	public static class Student {
		int id;
		String name;
		double cgpa;
		
		Student(int id, String name, double cgpa) {
			this.id = id;
			this.name = name;
			this.cgpa = cgpa;
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		ArrayList<Student> list = new ArrayList<Student>();
		for (int i = 0; i < n; i++) {
			int id = sc.nextInt();
			String name = sc.next();
			double cgpa = sc.nextDouble();
			list.add(new Student(id, name, cgpa));
		}
		Collections.sort(list, new StudentComparator());
		for (Student s : list) System.out.println(s.name);
	}
}
