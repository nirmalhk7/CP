# 204
# Easy Difficulty
# Completed Status.

def soln(n):
    prime=[]
    notPrime={}
    for i in range(2,n):
        try:
            factor=notPrime[i]
        except:
            prime.append(i)
            j=i
            while j<n:
                notPrime[j]=i
                j+=i
    return len(prime)

print(soln(10))