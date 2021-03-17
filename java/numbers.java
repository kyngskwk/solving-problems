import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class numbers {
	static StringTokenizer st;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int n_max, ans, N;
	static int[] nums = new int[100002];
	static int[] left = new int[100002];
	static int[] right = new int[100002];
	
	static void input() throws IOException {
		N = Integer.parseInt(br.readLine());
		
		st = new StringTokenizer(br.readLine());
		for(int i=1; i<=N; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		
		left[1] = nums[1];
		right[N] = nums[N];
		ans = 1; n_max = 1;
		
		for(int j=2; j<=N; j++) {
			left[j] = GCD(left[j-1], nums[j]);
			right[N-j+1] = GCD(right[N-j+2], nums[N-j+1]);
		}
		
		for(int k=1; k<=N; k++) {
			if (k==1) {
				if(nums[k] % right[2] == 0) continue;
				ans = right[2];
				n_max = nums[1];
				
			} else if(k<N) {
				int g = GCD(left[k-1], right[k+1]);
				if(nums[k] % g == 0) continue;
				
				if(g > ans) {
					ans = g;
					n_max = nums[k];
				}
			}else {
				int g = left[k-1];
				if(nums[k] % g == 0) continue;
				
				if(g > ans) {
					ans = g;
					n_max = nums[k];
				}
			}
		}
		
		if (ans==1) {
			ans = 0;
			n_max = 0;
		}
	}
	
	static int GCD(int a, int b) throws IOException {
		if(b==0) return a;
		return GCD(b, a%b);
	}
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		

		for (int tc=1; tc<=T; tc++) {
			input();
			System.out.printf("#%d %d %d\n", tc, ans, n_max);
			
		}

	}

}
