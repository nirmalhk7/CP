#include <bits/stdc++.h>

using namespace std;

int main()
{
  int T,N;
  cin>>T;
  int ans[T];
  for(int z=0;z<T;++z)
  {
    cin>>N;
    ans[z]=0;
    int l;
    vector<int> A;
    std::vector<int>::iterator it;
    for(int i=0;i<N;++i)
    {
      cin>>l;
      A.push_back(l);
    }
    sort(A.begin(),A.end());
    A.push_back(-1);
    for(int i=0;i<N;++i)
    {
      float x=(float)A[i]/(A[i]-1);
      cout<<"\nFLOATX- "<<x;

      cout << "\nCEILX- " << ceilf(x);
      if(ceilf(x)==x)
      {
        //cout<<"\nFinding "<<x;
        it=find(A.begin(),A.end(),(int)x);
        if(it!=A.end())
        {
          cout<<"\nA["<<i<<"]="<<A[i];
          cout << "\nMatched w A[" << it - A.begin() + 1 << "]=" << A[it - A.begin() + 1];
          A[it-A.begin()+1]=-1;
          ans[z]++;
        }
      }
    }
  }
  for(int z=0;z<T;++z)
  {
    cout<<ans[z]<<"\n";
  }
}