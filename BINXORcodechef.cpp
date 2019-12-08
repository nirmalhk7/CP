#include <bits/stdc++.h>

using namespace std;
int chartoint(char x)
{
  int z=x-48;
  return z;
}
int main()
{
  int T,N;
  cin>>T;
  int ans[T];
  for(int z=0;z<T;++z)
  {
    ans[z]=0;
    cin>>N;
    string A,B,res;
    cin>>A;
    cin>>B;
    vector<string> ansvec;
    for(int i=0;i<A.length();++i)
    {
      if(chartoint(A[i])!=chartoint(B[i]))
      {
        res.push_back('1');
      }
      else
      {
        res.push_back('0');
      }
      
    }
  }
}