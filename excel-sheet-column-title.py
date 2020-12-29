#306 
# Easy Difficulty
# Completed Status.

def soln(n):
    alphabet = [chr(l) for l in range(ord('A'), ord('Z') + 1)]
    
    num_list = [num for num in range(1, 27)]
    
    num_alpha = {}
    for num, alpha in zip(num_list, alphabet):
        num_alpha[num] = alpha
    
    stack = []
    while n > 26:
        r = n % 26
        if r == 0:
            r = 26
        stack.append(r)
        
        n = (n - r) // 26
        
    stack.append(n)
    
    res = ""
    for num in reversed(stack):
        res += num_alpha[num]
    
    return res