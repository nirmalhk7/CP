# 914
# Status: Doing

deck= []
deckFreq={}

for i in deck:
    try:
        deckFreq[i]+=1
    except:
        deckFreq[i]=1

lx=list(deckFreq.values())
freq= lx[0]
if(freq<2):
    print(False)
for i in range(1,len(lx)):
    if(lx[i]!=freq):
        print(False)


# if(lx[i])
print(True)
    