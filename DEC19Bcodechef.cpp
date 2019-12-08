#include <bits/stdc++.h>

using namespace std;

int main()
{
  int T,N,P,S;
  
  cin>>T;
  int sum[T];
  
  for(int k=0;k<T;++k)
  {
    sum[k]=0;
    cin>>N;
    int p[11] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    for(int i=0;i<N;++i)
    {
      
      cin>>P>>S;
      if(p[P]<S)
      {
        p[P]=S;
        ////cout<<"\np["<<P<<"]="<<S;
      }
      
    }
    for (int j = 0; j < 9; ++j)
    {
      sum[k]+=p[j];
    }
    //cout<<sum[k];
  }
  for(int i=0;i<T;++i)
  {
    cout<<sum[i]<<"\n";
  }
}
