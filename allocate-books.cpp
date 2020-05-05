#include<bits/stdc++.h>
using namespace std;

// Problem statement : Given fixed number of pages (V),  how many number of students we need?
// Solution :
//    simple simulation approach
//    intially Sum := 0
//    cnt_of_student = 0
//    iterate over all books:
//         If Sum + number_of_pages_in_current_book > V :
//                   increment cnt_of_student
//                   update Sum
//         Else:
//                   update Sum
//    EndLoop;
  


//     fix range LOW, HIGH
//     Loop until LOW < HIGH:
//             find MID_point
//             Is number of students required to keep max number of pages below MID < M ? 
//             IF Yes:
//                 update HIGH
//             Else
//                 update LOW
//     EndLoop;

int books(vector<int> &A, int B) {
    int output;
    int V=500;
    //TODO Check corner cases 
    if(A.size()<B)
    {
        output=-1;
    }
    else if(A.size()==B)
    {
        output=*max_element(A.begin(),A.end());      
    }
    else{
        int sum=0;
        int studentCount=0;
        for(int i=0;i<A.size();++i)
        {
            if(sum+A[i]>V)
            {
                studentCount++;
            }
            sum+=A[i];
        }
        int MID;
        for(int LOW=0,HIGH=A.size();LOW<HIGH;)
        {
            MID=(LOW+HIGH)/2;
            if(studentCount<MID)
            {
                HIGH=MID;
            }else
            {
                LOW=MID;
            }
            
        }
    }
    return output;
}

int main(){
    vector<int> inp{12, 34, 67, 90};
    cout<<books(inp,2);

}
