#include <iostream>
#include <cstring>

using namespace std;

bool check(char paper[],int s,int e)
{
    if(s>=e) return true;
    int l = s;
    int r = e;
    while(l<r)
    {
        if(paper[l]==paper[r]) return false;
        l++;
        r--;
    }
    return check(paper,s,r-1);
}

int main()
{
    char paper[3010];
    int t;
    scanf("%d",&t);
    for(int i=0; i<t; i++)
    {
        scanf("%s",&paper);
        int len = strlen(paper);
        if(len%2==0) printf("NO\n");
        else if(check(paper,0,len-1)) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
 

