package 기출;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


public class 다익스트라 {
	static StringTokenizer st;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int N, M, INF = Integer.MAX_VALUE;
	static ArrayList<Node>[] adj = new ArrayList[100002];
	static PriorityQueue<Node> pq = new PriorityQueue<>();
	static int[] list = new int[100002];
	
	static class Node implements Comparable<Node>{
		int n;
		int v;
		
		public Node(int a, int b) {
			n = a;
			v = b;
		}
		
		public int compareTo(Node next) {
			return v - next.v;
		}
	}
	
	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		Arrays.fill(list, INF);
		
		for(int i=1; i<=N; i++) adj[i].clear();
		
		int a, b, c;
		while(M-- > 0) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());
			
			adj[a].add(new Node(b, c));
			adj[b].add(new Node(a, c));
		}
		
		pq.add(new Node(1, 0));
		list[1] = 0;
		
		while(!pq.isEmpty()) {
			Node now = pq.poll();
			
			for(Node next: adj[now.n]) {
				int sum = next.v + list[now.n];
				if(sum < list[next.n]) {
					pq.offer(new Node(next.n, sum));
					list[next.n] = sum;
				}
			}
		}

	}
	
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		for(int i=0; i<100002; i++) adj[i] = new ArrayList<>();
		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=T; tc++) {
			input();
			if(list[N] == INF) list[N] = -1;
			System.out.printf("#%d %d", tc, list[N]);
		}
	}

}
