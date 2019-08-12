#include<bits/stdc++.h>
using namespace std;
int main()
{
	string x;
	getline (cin, x); 
	size_t found; 
	int z=0;
  
    found = x.find("00000000", found+1); 
    if (found != string::npos) 
    {
    	cout<<"(0)";
    	z=1;
    }
	found = x.find("11111111", found+1); 
    if (found != string::npos) 
    {
    	
    	cout<<"(1)";
    	z=1;
    }
	    
	if(z==1)
	{
		cout<<"YES";

	}
	else
	{
		cout<<"ZERO";
	}

}