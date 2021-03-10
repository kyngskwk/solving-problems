import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class iceBreak {
	static StringTokenizer st;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int N, H;
	static int[] cave, up, down;
	static int ans1, ans2;
	
	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		H = Integer.parseInt(st.nextToken());
		cave = new int[H+1];
		up = new int[H+1];
		down = new int[H+1];
		
//		st = new StringTokenizer(br.readLine());
		for(int i=0; i<N; i++) {
			int h = Integer.parseInt(br.readLine());
			if(i%2==0) {
				up[h]++; // 그 높이에 석순이 있거나 종유석이 있으면 +1 로 갯수 센다.
			}else {
				down[h]++;
			}
		}
	}
	
	static void check() throws IOException {
		// 위에서 부터 아래로 내려오면서 종유석의 값을 더한다  
		for(int i=H; i>0; i--) {
			up[i-1] += up[i];
			down[i-1] += down[i];
		}
		
		for(int j=1; j<=H; j++) {
			cave[j] = up[j] + down[H-j+1];
		}
		
		ans1 = 9999999;
		ans2 = 0;
		
		for(int k=1; k<=H; k++) {
			if(ans1 > cave[k]) {
				ans1 = cave[k];
				ans2 = 1;
			}else if (ans1 == cave[k]) {
				ans2++;
			}
		}
	}


	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for (int tc=1; tc<=T; tc++) {
			input();
			check();
			System.out.printf("#%d %d %d", tc, ans1, ans2);
		}
	}

}


