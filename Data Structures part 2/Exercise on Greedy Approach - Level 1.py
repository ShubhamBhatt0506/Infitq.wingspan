#lex_auth_0127667342200995843410

def make_change(denomination_list, amount):
    '''Remove pass and implement the Greedy approach to make the change for the amount using the currencies in the denomination list.
    The function should return the total number of notes needed to make the change. If change cannot be obtained for the given amount, then return -1. Return 1 if the amount is equal to one of the currencies available in the denomination list.  '''
    den=sorted(denomination_list,reverse=True)
    i=0
    count=0
    if den[-1]>amount:
        return -1
    while(amount>0):
        while(den[i]<=amount):
            amount-=den[i]  
            count+=1
            continue
        else:
            i+=1
    return count   

#Pass different values to the function and test your program
amount= 20
denomination_list = [1,15,10]
make_change(denomination_list, amount)
