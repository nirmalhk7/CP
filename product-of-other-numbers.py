
def soln(A):
    Alen= len(A)
    lowside= 1
    highside= 1
    for i in range(Alen):
        highside*=A[i]
    for i in range(len(A)):
        highside//=A[i]
        lowside*= A[i]
        # print("INIT",A[i])
        A[i]=highside
        # print("SETTING",highside,lowside,A[i])
        
    return A

def soln2(A):
    productBefore= 1
    productTotalWithZero= 1
    multiZero= True
    productTotalWithoutZero= 1
    if(len(A)<=1): raise Exception
    for i in range(len(A)):
        if(A[i]!=0): 
            productTotalWithoutZero*= A[i]
        else: 
            productTotalWithZero*= A[i]
            multiZero= not multiZero
    ans= []
    for i in range(len(A)):
        if(A[i]!=0):
            productTotalWithoutZero/=A[i]
            ans.append(int(productTotalWithZero*productBefore))
            productBefore*= A[i]
        elif(A[i]==0 and not multiZero):
            ans.append(int(productTotalWithoutZero*productBefore))
            productBefore= 0
        elif(A[i]==0 and multiZero):
            ans.append(0)
            productBefore= 0
    return ans

def get_products_of_all_ints_except_at_index(int_list):

    if len(int_list) < 2:
        raise Exception

    # We make a list with the length of the input list to
    # hold our products
    products_of_all_ints_except_at_index = [None] * len(int_list)

    # For each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product_so_far = 1
    for i in range(len(int_list)):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]

    # For each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product_so_far = 1
    for i in range(len(int_list) - 1, -1, -1):
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= int_list[i]

    return products_of_all_ints_except_at_index

if __name__ == "__main__":
    print(soln([1,7,3,4]))
    print(soln2([1,2,6,5,9]))
    print(soln2([6,0,0,-3]),[0, 0, 0, 0])
    print(soln2([1,2,3]),[6,3,2])