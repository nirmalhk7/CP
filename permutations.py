# def soln(A,B):
#     def rx(A,B,r=[],s=[],ind=0):
#         if(len(s)==B):
#             l=[]
#             l+=s
#             r.append(l)
#             return
#         for i in range(ind,len(A)):
#             s.append(A[i])
#             rx(A,B,r,s,i+1)
#             s.pop()
#         return s
#     return rx([i+1 for i in range(A)],B)
import math
def soln(A,ans=[]):

    def r(A,fixPosStart=0,fixPosEnd=1):
        if(fixPosStart!=fixPosEnd):
            for i in range(fixPosStart,fixPosEnd+1):
                A[1], A[i]= A[i], A[1]
                print(i,A)
                r(A,fixPosStart+1,fixPosEnd)
                A[1], A[i]= A[i], A[1]
        else:
            ans.append(A)
    r(A)
    return ans
if __name__ == "__main__":
    print(soln([1,2,3]))