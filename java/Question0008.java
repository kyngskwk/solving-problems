import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Question0008 {
	static StringTokenizer st;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int N, M, W, INF = Integer.MAX_VALUE;
	static ArrayList<Node>[] adj = new ArrayList[502];
	static int[] cnt = new int[502];
	static boolean ans;
	
	static class Node {
		int e;
		int v;
		
		public Node(int b, int c) {
			e = b;
			v = c;
		}
	}
	
	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		W = Integer.parseInt(st.nextToken());
		
		for(int i=1; i<=N; i++) {
			adj[i].clear();
			cnt[i] = INF;
		}
		
		int a, b, c;
		while(M-- > 0) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());
			
			adj[a].add(new Node(b, c));
			adj[b].add(new Node(a, c));
		}
		
		int s, e, w;
		while(W-- >0) {
			st = new StringTokenizer(br.readLine());
			s = Integer.parseInt(st.nextToken());
			e = Integer.parseInt(st.nextToken());
			w = Integer.parseInt(st.nextToken());
			
			adj[s].add(new Node(e, -1 * w));
		}
		
		ans = false;
		int i = 1;
		while(i<=N) {
			for(int j=1; j<=N; j++) {
				int k, r, vv;
				for(Node next: adj[j]) {
					k = j;
					r = next.e;
					vv = next.v;
					
					if(cnt[j] != INF) {
						if(cnt[r] > cnt[k] + vv) {
							cnt[r] = cnt[k] + vv;
							if(i == N) {
								ans = true; 
								return;
							}
						}
					}
					
				}
			}
			i++;
		}
		
		
	}
	

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		
		for(int i=0; i<502; i++) adj[i] = new ArrayList<>();
		
		for(int tc=1; tc<=T; tc++) {
			input();
			if(ans) System.out.printf("#%d YES\n", tc);
			else System.out.printf("#%d NO\n", tc);
			
		}

	}

}
