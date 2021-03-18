import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;


public class LCAalgorithm {
	static StringTokenizer st;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int N, Q;
	static int[][] P = new int[17][1000002];
	static int[] depth = new int[1000002];
	static ArrayList<Integer> [] adj = new ArrayList[100002];
	static ArrayDeque<Integer> q = new ArrayDeque<>();
 
	
	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		Q = Integer.parseInt(st.nextToken());
		
		for(int i=1; i<=N; i++) adj[i].clear();
		for(int i=0; i<17; i++) Arrays.fill(P[i], 0);
		Arrays.fill(depth, 0);
		
		st = new StringTokenizer(br.readLine());
		int now;
		for(int i=1; i<N; i++) {
			adj[Integer.parseInt(st.nextToken())].add(i+1);
		}
		
		q.add(1);
		depth[1] = 0;
		while(!q.isEmpty()) {
			int curr = q.poll();
			
			for(int ch: adj[curr]) {
				depth[ch] = depth[curr] + 1;
				P[0][ch] = curr;
				q.add(ch);
			}
			
		}
		
		for(int i=1; i<17; i++) {
			for(int j=0; j<=N; j++) {
				P[i][j] = P[i-1][P[i-1][j]]; 
			}
		}
		
		int a, b;
		while(Q-- > 0) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			lca(a, b);
		}
		
	}
	
	static int lca(int a, int b) throws IOException {
		if (depth[a] > depth[b]) {
			int tmp = a;
			a = b;
			b = tmp;
		}
		for(int i=16; i>=0; i--) {
			if(depth[b] - depth[a] >= (1<<i)) {
				b = P[i][b];
			}
		}
		if(a==b) return a;
		
		for(int i=16; i>=0; i--) {
			if (P[i][a] != P[i][b]) {
				a = P[i][a];
				b = P[i][b];
			}
		}
		return P[0][a];
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for(int i=1; i<100002; i++) adj[i] = new ArrayList<>;
		
		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<T; tc++) {
			input();
		}
	}

}
