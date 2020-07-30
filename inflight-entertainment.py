
def soln(movie_lengths,flight_length):
    if(flight_length<=0): return Exception
    if(len(movie_lengths)<2): return False

    # if(len(movie_lengths)==1): return movie_lengths[0]==flight_length
    movie_lengths.sort()
    i, j=0, len(movie_lengths)-1
    while i<j:
        if(movie_lengths[i]+movie_lengths[j]==flight_length):
            return True
        elif(movie_lengths[i]+movie_lengths[j]<flight_length):
            i+=1
        else:
            j-=1

    return False

if __name__ == "__main__":
    print(soln([1,2,3],3),True)
    print(soln([1],1),True)
    print(soln([1,2,3],2),False)