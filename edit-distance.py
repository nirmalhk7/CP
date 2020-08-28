
def soln(A,B):
    Alen, Blen= len(A), len(B)
    def recursive(Amark=0, Bmark=0,count=1000000000000000000):
        if(Amark<Alen and Bmark<Blen):
            return count
        if(Amark!=Bmark):
            # Insert
            count= min(count,recursive(Amark+1,Bmark+1,count+1))
            # Delete
            count= min(count,recursive(Amark+1,Bmark,count+1))
            # Replace
            count= 


if __name__ == "__main__":
    print(soln("gesek","geek"),1)