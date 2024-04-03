import random #here we have used the random function so thst every time we get a random shuffled values of it
import string #here we have used string to access all the total number of the elements 
# A program for the encryption and decryption of the password enter by the user
# here we are taking all kind od the characters 
char = " " + string.ascii_letters + string.digits + string.punctuation
# here we are making it a list to access the each and every sinlge element of this , because above we are not ablr to access the element seperatly  
char = list(char)
# here we are copying this with an another variable name so that we can work on this one 
# copy is the function which we used to copy 
key = char.copy()
# we are using random function to genrate random charachters all the time that our encrypted message would not be same all the time 
# this will always generate the new shufflled text or characters   
random.shuffle(key)
# here we have checked all the values by printing the both variable we decleared  
# print( f"char : {char}")
# zprint(f"key : {key}")
# form hereour encryption starts
# ENCRYPT
# we take an input from the user e.g text/password/phone_number/name etc
plain_text = input("Enter your message for the encryption : ")
# here we have decleared the cipher text as an empty text because we cannot fix itsa size a the input is from user so size of the text muct vary so we that   
cipher_text = " "
# here we have us the for loop ao that we can save each letters position through index
for letter in plain_text:
    # here we are saving it in index form 
    index = char.index(letter)
    # here we have now compare it with the cipher_text as it is shuffled 
    cipher_text += key[index]
#  here we have prin ted the original messages and the encrypted one
print( f"Your original message : {plain_text}")
print( f"Your encrypted message : {cipher_text}")  

# DECRYPT
# here we have taken the cipher_text from the user
cipher_text = input("Enter your message for the decryption : ")
# plain_text = input("Enter your message for the encryption : ")
# here we have decleared the plain text as an empty text because we cannot fix itsa size a the input is from user so size of the text muct vary so we that  
plain_text = " "
# here we have us the for loop ao that we can save each letters position through index
for letter in cipher_text:
    # here we are saving it in index form 
    index = key.index(letter)
    # here we have now compare it with the cipher_text as it is shuffled 
    plain_text += char[index]
#   here we have printed the original messages and the decrypted one
print( f"Your encrypted message : {cipher_text}")    
print( f"Your original message : {plain_text}") 