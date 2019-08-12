#include<iostream>
#include <stdio.h>
#include <ctype.h>
using namespace std;
int arr[10];
void addto(int x)
{
	if(x==1)
	{
		for(int i=0;i<10;++i)
		{
			if(arr[i]==0)
			{
				arr[i]=1;
				break;
			}
		}
		cout<<"\n";
	}
	else if(x==2)
	{
		for(int i=9;i>=0;--i)
		{
			if(arr[i]==0)
			{
				arr[i]=1;
				break;
			}
		}
		cout<<"\n";
	}
}
void printall()
{
	for(int i=0;i<10;++i)
	{
		cout<<arr[i];
	}
}
int main()
{
	for(int i=0;i<10;++i)
	{
		arr[i]=0;
	}
	int nos;
	cin>>nos;
	char mem[nos];
	scanf("%s",mem);
	for(int i=0;i<nos;++i)
	{
		if(mem[i]=='L')
		{
			addto(1);

		}
		else if(mem[i]=='R')
		{
					addto(2);
		}
		else if(isdigit(mem[i]))
		{
			int x=mem[i]-48;
			arr[x]=0;
		}
	}

	printall();
}
