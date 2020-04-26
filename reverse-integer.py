def reverse(A):
#  2,147,483,647 
# -2,147,483,648 -1,146,467,285
    if A > (2**31)-1 or A < -1*(2**31):
        return 0
    op=0
    negative=False
    if(A<0): 
        negative=True
        A*=-1
    while A!=0:
        op+=A%10
        A=(A-A%10)//10
        if(A!=0):
            op*=10
    if(negative):
        op*=-1
    return op

def isPalindrome(A):
    if(A<0):
        return 0
    else:
        return A==reverse(A)
if __name__ == "__main__":
    print(isPalindrome(121))

