package com.ssafy;

import java.util.Scanner;

public class Test {
    static long Answer;
    static int N, S;

    public static void main(String[] args) throws Exception {
        Scanner sc=new Scanner(System.in);
        int T=sc.nexInt(); // 테스트 케이스 수

        for(int test_case=1; test_case<=T; test_case++){
            N = sc.nexInt(); //배열 크기 NxN
            int[][] lake = new int[N][N] // default 0

            S = sc.nexInt() // 소금쟁이 수
            for (int k=0; k<S; k++){
                strider[k][0]=sc.nextInt();//행위치
                strider[k][1]=sc.nextInt();//열위치
                strider[k][2]=sc.nextInt();//방향(1:상,2:하,3:좌,4:우)
                
                int pi = strider[k][0];  //시작 위치 i
                int pj = strider[k][1];  //시작 위치 j
                int dir = strider[k][2]; //방향

                if(dir == 1){ // 상
                    pi = pi - 6;
                    if (pi>=0 && pi<N){
                        if(lake[pi][pj]==0){
                            lake[pi]pj] = 1;
                        }
                    }
                } else if(dir == 2){ // 하
                    pi = pi + 6;
                    if (pi>=0 && pi<N){
                        if(lake[pi][pj]==0){
                            lake[pi]pj] = 1;
                        }
                    }
                } else if(dir == 3){ // 좌
                    pj = pj - 6;
                    if (pj>=0 && pj<N){
                        if(lake[pi][pj]==0){
                            lake[pi]pj] = 1;
                        }
                    }
                } else{ // 우
                    pj = pj + 6;
                    if (pj>=0 && pj<N){
                        if(lake[pi][pj]==0){
                            lake[pi]pj] = 1;
                        }
                    }
                }
            }
            for (int i=0; i<lake.length; i++){
                for (int j=0; j<lake[i].length; j++){
                    Answer += lake[i][j];
                }
            }
            System.out.println("#"+test_case+" "+Answer);
        }

    }
}