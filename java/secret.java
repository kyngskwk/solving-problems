import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class secret {
	static StringTokenizer st;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static String K;
	static int L, ans;
	static boolean flag;
	static boolean[] noPrime = new boolean[100000];
	
	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
//		K = Integer.parseInt(st.nextToken());
		K = st.nextToken();
		L = Integer.parseInt(st.nextToken());
		
		ans = 0;
		flag = true;
		
		int len = K.length();
		for(int i=2; i<L; i++) {
			if(noPrime[i]) continue;
			int n = 0;
			for(int j=0; j<len; j++) {
				n = (n*10) + (K.charAt(j)-'0');
				n%=i;
			}
			if(n==0) {
				ans = i;
				flag = false;
				break;
			}
		}
	}
	

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		
		for(int i=2; i<100000; i++) {
			if(noPrime[i]) continue;
			for(int j=i+i; j<100000; j +=i) {
				noPrime[j] = true;
			}
		}
		
		for (int tc=1; tc<=T; tc++) {
			input();
			if(flag) {
				System.out.printf("#%d GOOD\n", tc);
			}else {
				System.out.printf("#%d BAD %d\n", tc, ans);
			}
			
		}

	}

}
