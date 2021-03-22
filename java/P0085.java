import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;


public class P0085 {
	static StringTokenizer st;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int N, M, D, K;
	static long[][][] DP = new long[202][202][2];
	static long ans, INF = Integer.MAX_VALUE;
	
	static class Node {
		int n;
		int v;
		
		public Node(int a, int b) {
			n = a;
			v = b;
		}
	}
	
	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		D = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		for(int i=0; i<=N; i++) {
			for(int j=0; j<=N; j++) {
				DP[i][j][0] = INF;
				DP[i][j][1] = INF;
			}
		}
		
		int a, b, c;
		for(int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());
			
			DP[a][b][0] = c;
			DP[b][a][0] = c;
			DP[a][b][1] = K;
			DP[b][a][1] = K;
		}
		
		
		for(int o=1; o<=N; o++) {
			for(int m=1; m<=N; m++) {
				for(int g=1; g<=N; g++) {
					DP[m][g][0] = Math.min(DP[m][g][0], DP[m][o][0] + DP[o][g][0]);
					DP[m][g][1] = Math.min(DP[m][g][1], DP[m][o][0] + DP[o][g][1]);
					DP[m][g][1] = Math.min(DP[m][g][1], DP[m][o][1] + DP[o][g][0]);
//					System.out.println(DP[m][g][0] + " " + DP[m][g][1]);
				}
			}
		}
		
		ans = 0;
		int x, y;
		for(int i=0; i<D; i++) {
			st = new StringTokenizer(br.readLine());
			x = Integer.parseInt(st.nextToken());
			y = Integer.parseInt(st.nextToken());
			ans += Math.min(DP[x][y][0], DP[x][y][1]);
		}
		
	}


	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=T; tc++) {
			input();
			System.out.printf("#%d %d", tc, ans);
		}
	 }

}
