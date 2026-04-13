%%writefile test.cpp

#include <bits/stdc++.h>
using namespace std;
#define ll long long

int opt;
ll dp[250][250][249][2],Inf=pow(10,18),x,X;

void dnc(int s,int e,int p,int q,int c,int i){
    int m=(s+e)/2;
    x=Inf;opt=p;

    for (int j=p;j<min(q,m);j++){
      X=dp[i][j][c-1][0]+dp[j][m][0][0];

      if (X<x){
        x=X;opt=j;
      }
    }

    dp[i][m][c][0]=x;dp[i][m][c][1]=opt;

    if (s+2<e) dnc(m+1,e,opt,q,c,i);
    if (s+1<e) dnc(s,m,p,opt+1,c,i);
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int v,p;
    ll l,a[250];

    cin>>v>>p>>l;
    for (int i=0;i<v;i++) cin>>a[i];

    if (p==1){
      x=Inf;opt=0;
      for (int i=0;i<v;i++){
        X=0;
        for (int j=0;j<v;j++){
          X+=min(llabs(a[j]-a[i]),l-llabs(a[j]-a[i]));
        }

        if (X<x){
          x=X;opt=i;
        }
      }
      cout<<x<<"\n"<<a[opt];

      return 0;
    }

    for (int i=0;i<v;i++){
      for (int j=i+1;j<v;j++){
        x=0;dp[i][j][0][1]=j;
        for (int k=i+1;k<j;k++){
          x+=min(a[k]-a[i],a[j]-a[k]);
        }
        dp[i][j][0][0]=x;
      }
    }

    for (int j=0;j<v;j++){
      for (int i=j+1;i<v;i++){
        x=0;dp[i][j][0][1]=j;
        for (int k=i;k<v;k++){
          x+=min(a[k]-a[i],l+a[j]-a[k]);
        }
        for (int k=0;k<=j;k++){
          x+=min(l+a[k]-a[i],a[j]-a[k]);
        }
        dp[i][j][0][0]=x;
      }
    }

    for (int c=1;c<p-1;c++){
      for (int i=0;i<v-c-1;i++){
        dnc(i+c+1,v,i+c,v,c,i);
      }
    }

    int q,w;
    x=Inf;
    for (int i=0;i<v-p+1;i++){
      for (int j=i+p-1;j<v;j++){
        X=dp[i][j][p-2][0]+dp[j][i][0][0];

        if (X<x){
          x=X;q=i;w=j;
        }
      }
    }

    cout<<x<<"\n";
    int id[250];

    id[p-1]=w;

    for (int j=p-2;j>0;j--){
      id[j]=dp[q][w][j][1];
      w=id[j];
    }

    cout<<a[q]<<" ";

    for (int i=1;i<p;i++) cout<<a[id[i]]<<" ";

    return 0;
}
