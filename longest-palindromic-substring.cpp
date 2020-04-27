#include<bits/stdc++.h>
using namespace std;

string q(string A){
    vector<int> centerList;
    string output="";
    if(A.size()==0)
    {      //      cout<<"E"<<endl;
        return output;
    }
    else if(A.size()==1)
    {       //     cout<<"D"<<endl;
        output=A[0];
        return output;
    }
    else if(A.size()==2)
    {
        output=A[0];
        if(A[0]==A[1])
        {
            output+=A[1];
                   //     cout<<"C"<<endl;
        }
        return output;
    }
    else if(A.size()>2)
    {
        for(int i=1;i<A.size()-1;++i)
        {
            if(A[i-1]==A[i+1])
            {
                centerList.push_back(i);
            }
        }
        if(centerList.size()>0)
        {
            int markup[centerList.size()];
              //          cout<<"B"<<endl;
            for(int i=0;i<centerList.size();++i)
            {
                markup[i]=0;
                for(int k=1;(centerList[i]+k)<A.size() && (centerList[i]-k>=0);++k)
                {
                    if(A[centerList[i]+k]==A[centerList[i]-k])
                    {
                        cout<<"Matched "<<A[centerList[i]+k]<<" "<<A[centerList[i]-k]<<" at "<<A[centerList[i]]<<" position "<<centerList[i]<<endl;
                    markup[i]+=1;
                    }
                }
            }
            int max_center=centerList[0];
            int max_markup=markup[0];
            for(int i=0;i<centerList.size();++i)
            {
                cout<<"Center "<<i+1<<" "<<A[centerList[i]]<<" at posn "<<centerList[i]<<" with markup "<<markup[i]<<endl;
                if(max_markup<markup[i])
                {
                    max_center=centerList[i];
                    max_markup=markup[i];
                }
            }
            
            //cout<<max_center<<" "<<max_markup;
            for(int i=max_center-max_markup+1;i<=max_center+max_markup-1;++i)
            {
                output+=A[i];
            }
            return output;
        }
        else
        {
            for(int i=1;i<A.size();++i)
            {
                output=A[i-1];
                if(A[i]==A[i-1])
                {
                    output+=A[i];
                  //  cout<<A[i-1]<<A[i]<<endl;
                    return output;
                }
            }
            output=A[0];
            return output;
        }
    }
    return "";
}
int main(){
    cout<<q("abbcccbbbcaaccbababcbcabca");
    //bbcccbb
}