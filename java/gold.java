import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class gold {
	static StringTokenizer st;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int N, M, ans;
	
	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		int g = GCD(N, M);
		ans = (M/g - 1) * g;
	}
	
	static int GCD(int a, int b) {
		if(b==0) return a;
		return GCD(b, a%b);
	}

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for (int tc=1; tc<=T; tc++) {
			input();
			System.out.printf("#%d %d", tc, ans);
		}

	}

}
