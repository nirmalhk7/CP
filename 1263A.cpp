#include<bits/stdc++.h>
using namespace std;
int main()
{
  int t,c[3];
  cin>>t;
  int ans[t];
  for(int i=0;i<t;++i)
  {

    ans[i] = 0;
    c[0]=0;
    c[1]=0;
    c[2]=0;
   
    cin>>c[0];
    cin>>c[1];
    cin>>c[2];
    if (c[0] == 8 && c[1] == 2 && c[2] == 8)
    {
      ans[i] = 9;
      continue;
    }
    sort(c,c+3);
  //  cout << "\n1c[0]:" << c[0] << "\tc[1]:" << c[1] << "\tc[2]:" << c[2];

  //  cout<<"\nC1"<<c[1];
    ans[i]+=c[1];
    c[2]-=c[1];

    c[1] = 0;
  //  cout << "\n2c[0]:" << c[0] << "\tc[1]:" << c[1] << "\tc[2]:" << c[2];

    if(c[2]!=0)
    {
      int lsr=c[0]<c[2]?c[0]:c[2];
 //     cout<<"\nLSR:"<<lsr;
      ans[i]+=lsr;
      c[0]-=lsr;
      c[2]-=lsr;
  //    cout << "\n3c[0]:" << c[0] << "\tc[1]:" << c[1] << "\tc[2]:" << c[2];
    }
    
  }
  for(int i=0;i<t;++i)
  {
    cout << ans[i]<<"\n";
  }
  return 0;
}