def soln(A):
    A= sorted(A)
    answer=[]
    for mstart,mend in A:
        if(answer==[]):
            answer.append((mstart,mend))
            continue
        top=answer[-1]
      #  print("TOP",top)
        # If start and end is between previous meeting
        if(top[0]<=mstart<=top[1] and top[0]<=mend<=top[1]):
            continue
        elif(top[0]<=mstart<=top[1]):
            answer.pop()
            answer.append((top[0],mend))
        else:
            answer.append((mstart,mend))
    return answer
if __name__ == "__main__":
    print(soln([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
    print(soln([(0,2),(1,4),(2,3),(5,9),(6,7)]))
    print(soln([(1,2),(2,3)]))
    print(soln(  [(1, 5), (2, 3)]))