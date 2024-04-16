"""
Project 1 Applied Cryptography
Student Name: Alejandro Cabrera
Student ID: U0000008370
Purpose: Write a program to create a Vigenere cypher
"""

def main():
    """The main function of this program"""
    #prompt the user for a message
    message = input("Please enter a message (without spaces and all caps): ")
    basekey = "VIGENERE"
    key=""
    #If my last name is same length as message
    if (len(message)==len(basekey)):
        key=basekey
    #If my last name is a larger length then the message
    elif (len(message)<len(basekey)):
        for i in range (0,len(message)):
            key = key+basekey[i]
    #If my last name is a smaller length then the message
    else:
        k=0
        for i in range (0,len(message)):
            if k==len(basekey):
                k=0
            key = key+basekey[k]
            k=k+1
        
    #convert the message to ciphertext
    ciphertxt = encrypt(message,key)
    
    #display the result
    print("The original message:",message,"has been converted into",ciphertxt)

def encrypt(message,key):
    """Encrypt the original message into cyphertext"""
    
    #the mapping between letters and their integer values
    letterToNumber = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,
                'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,
                'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,
                'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,
                'Y':24,'Z':25,}

    #the mapping between integers and their letter values
    numberToLetter = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',
                6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',
                12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',
                18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',
                24:'Y',25:'Z',}

    
    cipherText=""
    
    for i in range (0,len(message)):
        #convert the letters to integers for math
        newLetterNum = (letterToNumber[message[i]]+letterToNumber[key[i]])%26
        #convert the new numbers back to integers
        cipherText= cipherText+numberToLetter[(newLetterNum)]

    return cipherText

#entry point of execution
main()
