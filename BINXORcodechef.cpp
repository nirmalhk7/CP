#include <bits/stdc++.h>

using namespace std;
int chartoint(char x)
{
  int z=x-48;
  return z;
}
vector<string> strvector;
vector<string> countPermutn(string str,string ans,vector<string> resvec)
{
  if(str.size()==0)
  {
    //cout<<"\n"<<ans;
    vector<string>::iterator it;

    it = find(resvec.begin(), resvec.end(), 30);
    if (it == resvec.end())
    {
      cout<<"\nNEW\t";
      resvec.push_back(ans);
    }
  }
  for(int i=0;i<str.length();++i)
  {
    char ch=str.at(i);
    string ros=str.substr(0,i)+str.substr(i+1);
    cout<<"\nROS="<<ros;
    countPermutn(ros,ans+ch,resvec);
  }
  return resvec;
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
    vector<string> psbA,psbB;
    psbA=countPermutn(A,"",psbA);
    psbB=countPermutn(B,"",psbB);
    
    for(int i=0;i<A.length();++i)
    {
      if(A[i]!=B[i])
      {
        res.push_back('1');
      }
      else
      {
        res.push_back('0');
      }
      
    }
    cout<<"\nFound "<<strvector.size()<<" Combo!";
  }
}