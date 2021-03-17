import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;


public class top {
	static StringTokenizer st;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int N, ans;
	static Stack<Integer> stack1; 
	static Stack<Integer> stack2; // 발사 못한 총알들 
	
	
	static void input() throws IOException {
		N = Integer.parseInt(br.readLine());
		stack1 = new Stack<>();
		stack2 = new Stack<>();
		
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<N; i++) {
			stack1.add(Integer.parseInt(st.nextToken()));
		}
	}
	
	static void check() throws IOException {
		ans = 0;
		
		for(int i=N-1; i>=0 ; i--) {
			int now = stack1.pop();
			if (stack1.isEmpty()) {
				break;
			}
			if(stack1.peek() >= now) {
				ans += i;
				
				while(!stack2.isEmpty()) {
					if(stack1.peek() >= stack2.peek()) {
						ans += i;
						stack2.pop();
					}else break;
				}
			}else {
				stack2.add(now);
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc>=T; tc++) {
			input();
			check();
			System.out.printf("#%d %d", tc, ans);
		}
	}

}
