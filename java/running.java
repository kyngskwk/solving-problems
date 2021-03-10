import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class running {
	static StringTokenizer st;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int N, ans;
	static int[] power;
	static int[] temp;
	
	static void input() throws IOException {
		N = Integer.parseInt(br.readLine());
		power = new int[N];
		temp = new int[power.length];
		
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<N; i++) {
			power[i] = Integer.parseInt(st.nextToken());
		}
	}
	
	static void mergeSorting(int start, int end) throws IOException {
		if(start==end) return;
		
		int l = start;
		int mid = (start+end)/2;
		int r = mid+1;
		
		mergeSorting(l, mid);
		mergeSorting(r, end);
		
		int tmpIdx = 0;
		
		while(l<=mid && r<=end) {
			if(power[l] < power[r]) {
				ans = ans + mid - l + 1;
				temp[tmpIdx++] = power[r++];
			}else {
				temp[tmpIdx++] = power[l++];
			}
		}
		while(l<=mid) {
			temp[tmpIdx++] = power[l++];
		}
		while(r<=end) {
			temp[tmpIdx++] = power[r++];
		}
		
		for(int i=0; i<tmpIdx; i++) {
			power[i+start] = temp[i]; 
		}
	}

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		
		for(int tc=1; tc<=T; tc++) {
			ans = 0;
			input();
			mergeSorting(0, N-1);
			System.out.printf("#%d %d\n", tc, ans);
		}

	}

}
