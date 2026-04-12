%%writefile test.cpp

#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll a[100000],b[100000],c[100000];

ll C(int x,int y){
  return (c[x]-c[y])/(b[y]-b[x]);
}

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int n;cin>>n;

  for (int i=0;i<n;i++) cin>>a[i];
  for (int i=0;i<n;i++) cin>>b[i];

  deque<int> d={0};

  for(int i=1;i<n;i++){

    while (d.size()>1 and a[i]>C(d[0],d[1])) d.pop_front();

    int j=d[0];
    c[i]+=c[j]+a[i]*b[j];

    while (d.size()>1 and C(i,d.back())<=C(d.back(),d[d.size()-2])) d.pop_back();

    d.push_back(i);
  }

  cout<<c[n-1];

  return 0;
}
