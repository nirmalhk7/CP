
#include<bits/stdc++.h>
using namespace std;

string rotate(string str){
    string part1=str.substr(0,1);
    string part2=str.substr(1,str.size());
    return part2+part1;
}
int filterValues(vector<int> strval, int limit)
{
    vector<int> ans;
    int arr[*max_element(strval.begin(), strval.end())];
    for(int i=0;i<*max_element(strval.begin(), strval.end());++i)
    {
        arr[i]=0;
    }
    for(int i=0;i<strval.size();++i)
    {
        arr[strval[i]-1]++;
    }
    for(int i=0;i<*max_element(strval.begin(), strval.end());++i)
    {
        if(arr[i]>=limit)
        {
            ans.push_back(i+1);
        }
    }
    return *min_element(ans.begin(),ans.end());
}
int solve(vector<string> &A) {
    int stringlength_size=A[0].size();
    for(int i=1;i<A.size();++i)
    {
        if(stringlength_size<A[i].size())
        {
            stringlength_size=A[i].size();
        }
    }
    cout<<stringlength_size<<endl;
    vector<int> strval;
    vector<string> A_copy=A;
    for(int j=0;j<A.size();++j)
    {
        for(int i=1;i<=stringlength_size;++i)
        {
            string rtStr=rotate(A_copy[j]);
            if(rtStr==A[j])
            {
                strval.push_back(i);
            }
            else{
                A_copy[j]=rotate(A_copy[j]);
            }
        }
    }
    for(int i=0;i<strval.size();++i){
        cout<<strval[i]<<" ";
    }
    cout<<endl;
    return filterValues(strval,A.size());
}

int main(){
    vector<string> inp{"a","ababa","aba"};
    cout<<solve(inp);
}