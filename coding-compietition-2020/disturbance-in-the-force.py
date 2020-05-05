
def force(m,a):
    

if __name__ == "__main__":
    N=int(input())
    masses=list(map(int, input().split()))
    accs=[]
    for i in range(N):
        x,y=input().split()
        accs.append([int(x),int(y)])
    force(masses,accs)