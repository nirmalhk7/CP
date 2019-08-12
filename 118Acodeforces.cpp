#include<bits/stdc++.h>
using namespace std;
int main()
{
	char x[100],y[100];
	cin>>x;
	for(int i=0;x[i]!='\0';++i)
	{
		if(isupper(x[i]))
		{
			x[i]=tolower(x[i]);
		}
		//Not a vowel
		if(x[i]!='A'&&x[i]!='E'&&x[i]!='I'&&x[i]!='O'&&x[i]!='U'&&x[i]!='Y'&&x[i]!='a'&&x[i]!='e'&&x[i]!='i'&&x[i]!='o'&&x[i]!='u'&&x[i]!='y')
		{
			cout<<"."<<x[i];
		}

	}
}