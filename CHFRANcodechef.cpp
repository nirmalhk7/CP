#include <bits/stdc++.h>

using namespace std;
int main()
{
  int T;
  cin >> T;
  int N;
  for (int t = 0; t < T; t++)
  {
    cin>>N;
    pair<int,int> range[N];
    vector<pair<int, int>> subset[2];
    for(int i=0;i<N;++i)
    {
      cin>>range[i].first;
      cin>>range[i].second;
      
      subset[i%2].push_back(range[i]);
    }
    
    
  }
}