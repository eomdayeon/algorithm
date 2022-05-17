#include <iostream>
#include <cstring>
#include <cmath>
#define MAX 257
using namespace std;

int map[MAX][MAX] ={0};
int cnt = 0;


bool isdrain(int x, int y, int len){
    for(int i=x;i<x+len;i++){
        for(int j=y;j<y+len;j++){
            if(map[i][j]!=0) return true;
        }
    }
    return false;
}

void solve(int x,int y, int len){
    cnt++;
    int halflen = len/2;
    if(!isdrain(x,y,halflen)) {
        map[x+halflen-1][y+halflen-1] = cnt;
    }
    if(!isdrain(x,y+halflen,halflen)) {
        map[x+halflen-1][y+halflen] = cnt;
    }
    if(!isdrain(x+halflen,y,halflen)) {
        map[x+halflen][y+halflen-1] = cnt;
    }

    if(!isdrain(x+halflen,y+halflen,halflen)) {
        map[x+halflen][y+halflen] = cnt;
    }
    if(len == 2) return;
    solve(x,y,halflen);
    solve(x+halflen,y,halflen);
    solve(x,y+halflen,halflen);
    solve(x+halflen,y+halflen,halflen);
}



int main(){
    int K;
    int d1, d2;
    scanf("%d",&K);

    scanf("%d %d",&d1,&d2);
    map[d2][d1] =  -1;
    //printf("%d\n",(pow(2,K)));
    solve(1,1,int(pow(2,K)));

    for(int i=int(pow(2,K));i>0;i--){
        for(int j=1;j<=int(pow(2,K));j++){
            printf("%d ",map[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}
