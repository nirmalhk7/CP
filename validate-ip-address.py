# 166
# Status: Ran out of tme, had to refer.

def soln(x):
    xipv4arr = x.split(".")
    xipv6arr = x.split(":")
    if(len(xipv4arr) != 4 and len(xipv6arr) != 8):
        return "Neither"
    if(len(xipv4arr) == 4):
        for sub in xipv4arr:
            try:
                sub_int = int(sub)
                # print(sub, sub_int)
                if(sub_int < 0 or sub_int > 255 or str(sub_int) != sub):
                    return "Neither"
            except:
                return "Neither"

        return "IPv4"
    elif(len(xipv6arr) == 8):
        for sub in xipv6arr:
            try:
                sub_int = int("0x"+sub,16)
            except:
                # print(sub)
                return "Neither"
            if(4<len(sub) or len(sub)<1):
                # print("x",sub)
                return "Neither"
        return "IPv6"


print(soln("172.16.254.1"),"IPv4")
print(soln("2001:0db8:85a3:0:0:8A2E:0370:7334"),"IPv6")
print(soln("256.256.256.256"),"Neither")
print(soln("2001:0db8:85a3:0:0:8A2E:0370:7334:"),"Neither")
print(soln("1e1.4.5.6"),"Neither")
print(soln("192.168.01.1"),"Neither")
print(soln("2001:0db8:85a3:0000:0000:8a2e:0370:7334"),"IPv6")
print(soln("2001:db8:85a3:0:0:8A2E:0370:7334"),"IPv6")
print(soln("2001:0db8:85a3::8A2E:037j:7334"),"Neither")
print(soln("02001:0db8:85a3:0000:0000:8a2e:0370:7334"),"Neither") 