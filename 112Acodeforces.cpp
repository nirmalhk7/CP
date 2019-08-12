#include<bits/stdc++.h>
using namespace std;
int main()
{
	char x[100],y[100];
	cin>>x;
	cin>>y;
	int total,a=0,b=0;
	for(int i=0;x[i]!='\0';++i)
	{
		if(isupper(x[i]))
		{
			x[i]=tolower(x[i]);
		}
		if(isupper(y[i]))
		{
			y[i]=tolower(y[i]);
		}
	}
	for(int i=0;x[i]!='\0';++i)
	{
		a+=x[i];
		b+=y[i];

	}
	total=a-b;
	cout<<"\nA="<<a<<"\tB="<<b;
	if(total<0)
	{
		cout<<"1";
	}
	else if(total>0)
	{
		cout<<"-1";
	}
	else if(total==0)
	{
		cout<<"0";
	}
}