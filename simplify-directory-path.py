
def soln(A):
    A= A[1:-1]
    Arr= A.split('/')
    chx= []
    chxlen= 0
    for i in Arr:
        if(i=="."):
            print("IGN",i,"/"+"/".join(chx))
            continue
        elif(i==".."):
            if(chxlen!=0):
                chx.pop()
                chxlen-=1
            print("BACK",i,"/"+"/".join(chx))
            
        else:
            chx.append(i)
            chxlen+= 1
            print("CHAR",i,"/"+"/".join(chx))
    return "/"+"/".join(chx)
        
if __name__ == "__main__":
    # print(soln("/a/./b/../../c/"))
    # print(soln("/home/"))
    # print(soln("/../"))
    # print(soln("/a/b/./c/../"))
    print(soln("/sug/../lck/./tii/../../../mqp/.././kao/fhc/./lth/zlw/./olp/rzu/./dpl/dka/yuc/../mjq/zcs/dkp/.././mqb/../qyu/.././.././.././wzr/.././nhj/rdv/ull/xld/tjc/ple/tii/thn/../../../../bal/fwf/./../uhd/szm/././qcq/././dao/../gok/vmv/bhy/zpa/izh/../uat/././../../ydu/vdu/gpj/jyn/.."))
    print("/kao/fhc/lth/zlw/olp/rzu/dpl/dka/nhj/rdv/ull/xld/bal/uhd/szm/qcq/gok/vmv/bhy/ydu/vdu/gpj")