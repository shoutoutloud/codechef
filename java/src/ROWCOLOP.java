import java.util.Arrays;
import java.util.Scanner;
public class ROWCOLOP {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int r[] = new int[n];
		int s[] = new int[n];
		int q = sc.nextInt();
		while(q-->0){
			String a = sc.next();
			int b = sc.nextInt();
			int c = sc.nextInt();
			if (a.charAt(0)=='R'){
				r[b-1]+=c;
			}
			else{
				s[b-1]+=c;
			}
		}
		Arrays.sort(r);
		Arrays.sort(s);
		System.out.println(r[n-1]+s[n-1]);
	}
}


