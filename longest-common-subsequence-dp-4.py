def lcs(X,Y,m,n):
    if m==0 or n==0:
        return 0
    elif X[m-1] == Y[n-1]: return 1+ lcs(X,Y,m-1,n-1)
    else: 
        str1= 
        return max(lcs(X,Y,m,n-1),lcs(X,Y,m-1,n))

if __name__ == "__main__":
    X='ABCDGH'
    Y='AEDFHR'
    print(lcs(X,Y,len(X),len(Y)))