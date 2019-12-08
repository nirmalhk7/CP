#include<bits/stdc++.h>
using namespace std;
int main()
{
  int T;
  do{
    cin>>T;
    int N,M,Q;
    cin>>N>>M>>Q;
    int arr[N][M];
    for(int i=0;i<Q;++i)
    {
      int X,Y;
      cin>>X>>Y;
      --X;--Y;
   //   cout<<"\nXX="<<X<<" YY="<<Y;
      for(int p=0;p<M;++p)
      {
        //Incrementing Row
        arr[X][p] += 1;
      //  cout << "\nIncrementing1 (" << X << "," << p << ").\n";
      }
      for(int q=0;q<N;++q)
      {
        //Incrementing Column
        arr[q][Y]+=1;
       // cout<<"\nIncrementing2 ("<<q<<","<<Y<<").\n";
      }
    }
    int ans=0;
    //Finding No. of Odd Numbers
    for(int i=0;i<N;++i)
    {
      for(int j=0;j<M;++j)
      {
   //     cout<<"\narr["<<i<<"]["<<j<<"]="<<arr[i][j];
        if((arr[i][j]%2)!=0)
        {
          ans++;
        }
      }
    }
    cout<<ans;
    --T;
  }while(T>0);
}