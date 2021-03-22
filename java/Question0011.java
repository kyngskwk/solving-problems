import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Question0011 {
	static StringTokenizer st;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int N, M;
	static int[] list = new int[11];
	static int[] dp = new int[640001];
	
	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<N; i++) {
			list[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.fill(list, 0, M+1, 999999999);
		
		for(int i=0; i<N; i++) dp[list[i]] = 1;
		
		for(int i=0; i<N; i++) {
			for(int j=list[i]; j<=M; j++) {
				dp[j] = Math.min(dp[j], dp[j - list[i]] + 1);
			}
		}
	}
	

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		
		for(int tc=1; tc<=T; tc++) {
			input();
			System.out.printf("#%d %d", tc, dp[M]);
		}
		

	}

}
