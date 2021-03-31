#lex_auth_0127667326864670723497

def find_unknown_words(text,vocabulary):
    #Remove pass and write your logic here
    ans=[]
    for i in text.split():
        if i not in vocabulary:
            ans.append(i)
    if ans==[]:
        return -1
    return set(ans)

#Pass different values of text and vocabulary to the function and test your program
text="The sun rises in the east and sets in the west."
vocabulary = ["sun","in","rises","the","east"]
unknown_words=find_unknown_words(text,vocabulary)
print("The unknown words in the file are:",unknown_words)
