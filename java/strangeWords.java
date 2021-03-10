import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class strangeWords {
	static StringTokenizer st;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int N, K, ans;
	static int[] list;
	static int[] cnt;
	
	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		for(int i=0; i<N; i++) {
			list[i] = Integer.parseInt(br.readLine());
		}
		
	}
	
	static void find() throws IOException {
		int l=0, r=0;
		int kind = 0;
		ans = 999999;
		//끝을 넘으면 알고리즘 끝 
		//N보다 작을떼 까지 반복 
		while(r<N) {
			while(r<N && kind<N) {
				// 포함된 단어의 종류가 k개 넘으면 끝
				int word = list[++r];
				
			}
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
