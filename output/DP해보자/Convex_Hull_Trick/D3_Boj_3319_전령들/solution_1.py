%%writefile test.cpp

#include <bits/stdc++.h>
using namespace std;
#define ll long long

bool vis[100000]={1};
ll V[100000],l[100000],c[100000];
vector<int> Ind={0};
vector<array<int,2>> graph[100000];

long double C(int i,int j){
  return (long double)(c[i]-c[j])/(l[i]-l[j]);
}

void dfs(int i,int e){
  for (auto a:graph[i]){
    int x=a[0];

    if (vis[x]==0){
      vis[x]=1;
      l[x]=l[i]+a[1];

      int p=0,q=e,sv;

      while (p<q){
        int m=(p+q)>>1;
        if (C(Ind[m],Ind[m+1])<V[x]) p=m+1;
        else q=m;
      }

      int y=Ind[p];
      c[x]+=V[x]*l[x]+c[y]-V[x]*l[y];

      q=e+1;
      while (p+1<q){
          int m=(p+q)>>1;
          if (C(x,Ind[m])<=C(Ind[m],Ind[m-1])) q=m;
          else p=m;
      }

      if (Ind.size()==q){
        sv=-1;
        Ind.push_back(x);
      }

      else{
        sv=Ind[q];
        Ind[q]=x;
      }

      dfs(x,q);

      if (sv!=-1) Ind[q]=sv;
      else Ind.pop_back();
    }
  }
}


int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n,u,v,d;
    cin>>n;

    for (int i=1;i<n;i++){
      cin>>u>>v>>d;
      graph[u-1].push_back({v-1,d});
      graph[v-1].push_back({u-1,d});
    }

    for (int i=1;i<n;i++){
      cin>>c[i]>>V[i];
    }

    l[0]=0;c[0]=0;
    dfs(0,0);

    for (int i=1;i<n;i++){
      cout<<c[i]<<" ";
    }

    return 0;
}
