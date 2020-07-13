def soln(A):
    A=str(A)
    Aarr="0"*(32-len(A))+A
    Aarr=[i for i in Aarr]
    Aarr.reverse()
    return int("".join(Aarr),2)
if __name__ == "__main__":
    print(soln(00000010100101000001111010011100'))
    print("00111001011110000010100101000000")