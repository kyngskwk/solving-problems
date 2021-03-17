import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;



public class superevent {
	static StringTokenizer st;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int Q, a, b, idx, max, now;
	static int[] cards = new int[1000002];
	static long[] tree = new long[4000000];
	static Queue<Integer> ans;
	
	static void input() throws IOException {
		Q = Integer.parseInt(br.readLine().trim());
		ans = new LinkedList<>();
		
		max = 0;
		
		Arrays.fill(cards, 0);
		
		
		for(int i=0; i<Q; i++) {
			st = new StringTokenizer(br.readLine().trim(), " ");
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			
//			System.out.printf("a = %d", a);
			if(a == 1) {
				if(max < b) {
					max = b;
				}
				cards[b]++;
//				System.out.print(cards[b]);
			} else {
				makeTree(b);
//				findCard(b);
				
				ans.offer(now - idx + 1);
			}
		}
	}
	
	static void makeTree(int b) throws IOException {
		Arrays.fill(tree, 0);
		idx = 1;
		while(idx < max) {
			idx *= 2;
		}
		
		for(int i=0; i<max; i++) {
			int num = cards[i+1];
			tree[idx+i] = num;

		}
		
		for (int j=idx-1; j>=0; j--) {
			tree[j] += tree[j*2] + tree[j*2+1];

		}
		
		now = 1;
		
		while(b>=0) {
			
			if(now >= idx) {
//				System.out.print("end");
				return;
			}
			if(tree[2*now] >= b) {
				now = 2*now;
			} else {
				b -= tree[2*now];
				now = 2*now + 1;
			}
			
		}
		System.out.print("end");
	}
	
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine().trim());
		for (int tc = 1; tc<=T; tc++) {
			input();
			System.out.printf("#%d ", tc);
			while(!ans.isEmpty()) {
				System.out.printf("%d ", ans.poll());
			}
			System.out.print("\n");
		}
		

	}

}




