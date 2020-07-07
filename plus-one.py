def soln(digits):
    if(len(digits)==0): return 0
    else:
        digitInt= int(''.join(str(elem) for elem in digits))+1
        ans=[]
        while digitInt!=0:
            ans.append(digitInt%10)
            digitInt//=10
        ans.reverse()
        return ans

if __name__ == "__main__":
    print(soln([1,8,9,9]))