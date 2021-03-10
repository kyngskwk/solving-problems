import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class buildHouse {
	static StringTokenizer st;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int X, N, L1, L2;
	static int[] woods;
	static boolean ans;
	
	static void input() throws IOException {
		X = Integer.parseInt(br.readLine());
		N = Integer.parseInt(br.readLine());
		woods = new int[N];
		
		for(int i=0; i<N; i++) {
			woods[i] = Integer.parseInt(br.readLine());
		}
		
		Arrays.sort(woods);
	}
	
	static void find() throws IOException {
		ans = false;
		int nx = X * 10000000;
				
		for(int i=0; i<N; i++) {
			// 딱 반일 때  
			if(woods[i]*2 == nx) {
				if(woods[i] == woods[i+1]) {
					ans = true;
					L1 = woods[i];
					L2 = woods[i];
					return;
				}
				continue;
			}
			// 이진검색 사용하면 -> 찾으면 index리턴, 없으면 음수 리턴 
			if(Arrays.binarySearch(woods, 0, N, nx-woods[i]) > 0) {
				// 양수, 즉 값이 있으면 
				ans = true;
				L1 = woods[i];
				L2 = nx - woods[i];
				return;
			}
		}
	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=T; tc++) {
			input();
			find();
			if(ans) {
				System.out.printf("#%d yes %d %d",tc, L1, L2);
			}else {
				System.out.printf("#%d danger",tc);
			}
		}

	}

}

