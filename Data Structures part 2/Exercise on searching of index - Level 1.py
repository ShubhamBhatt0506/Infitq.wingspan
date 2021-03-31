#lex_auth_0127667385795952643524

def find_decreasing_start(list1,start,end):
    #Remove pass and write your logic here
    l=start
    h=end
    
    while(l<=h):
        mid=(l+h)//2
        if list1[mid]>list1[mid+1] and list1[mid]>list1[mid-1]:
            print(1)
            return mid+1
        
        elif list1[mid]>list1[l]:
            l=mid+1
        else:
            h=mid-1
            

#Use different values for list1 and test your program
list1=[1,4,7,8,9,5,4]
start=0
end=len(list1)-1
result=find_decreasing_start(list1,start,end)
print("The index position at which the increasing array starts decreasing is:",result)
