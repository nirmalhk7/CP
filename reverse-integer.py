#7 Easy Difficulty: Could do. Completed Status. This'd be slightly harder on C++/JAVA
def reverse(x):
    isNegative= x<0
    if(isNegative):
        x*=-1
    rev_int=int(str(x)[::-1])
    if(isNegative):
        rev_int*=-1
    if(not(-2**31<rev_int<2**31)):
        rev_int=0
    return rev_int

print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(0))