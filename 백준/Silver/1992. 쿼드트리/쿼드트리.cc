#include <iostream>
#include <cstring>
#define MAX 64
using namespace std;

int map[MAX][MAX];
void solve(int size,int x, int y);

int main(){
    int N;
    scanf("%d",&N);
    for(int i=0;i<N;i++){
        string s;
        cin >> s;
        for(int j=0;j<N;j++){
            map[i][j] = s[j]-'0';
        }
    }
    solve(N,0,0);
}

void solve(int size,int x, int y){
    int s = size;
    int flag = 0;
    if(size == 1){
        printf("%d",map[x][y]);
        return;
    }
    bool OnlyZero= true; bool OnlyOne=true;
    for(int i=x; i<x+s; i++){
        for(int j=y;j<y+s; j++){
            if(map[i][j]==1) OnlyZero = false;
            if(map[i][j]==0) OnlyOne = false;
        }
    }
    if(OnlyZero == true) {
        printf("0");
        return;
    }
    if(OnlyOne == true){
        printf("1");
        return;
    }

    s=s/2;
    printf("(");
    solve(s,x,y);
    solve(s,x,y+s);
    solve(s,x+s,y);
    solve(s,x+s,y+s);
    printf(")");
}