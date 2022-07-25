"""This file asks the user for a string of words and returns
them in reverse order"""

def spitOutReverse() :
    words = str(input("Enter a string of words: "))
    wordlist = []
    currentWord = ""
    for char in words : 
        if char != " " :
            currentWord += char
        else:
            wordlist.insert(0,currentWord)
            currentWord = ""
    wordlist.insert(0,currentWord)
    return " ".join(wordlist)
    
    
print (spitOutReverse())

       
