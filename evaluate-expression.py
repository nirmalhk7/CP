def isOperand(x): 
    return ()  
  
# Get Infix for a given postfix  
# expression  
def getInfix(exp) : 
    s = []  
    calc=0
    for i in exp:      
        if (i!='+' and i!='-' and i!='/' and i!='*') :          
            s.insert(0, i)  
        else: 
            op1 = s[0]  
            s.pop(0)  
            op2 = s[0]  
            s.pop(0)
            if(i=='/'):
                s.insert(0, "(" + op2 +"//"+ op1 + ")")
                calc=int(op2)//int(op1)
            else:  
                s.insert(0, "(" + op2 + i + op1 + ")")  
                calc=eval(op2+i+op1)
            # print(s[0])

    return calc 
if __name__ == "__main__":
    print(getInfix(["4", "13", "5", "/", "+"]))
    print(getInfix(["2", "1", "+", "3", "*"]))