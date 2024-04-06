# Aa password complexcity Checker 
import string
# Here we are taking input of the password from the user 
password = input("Enter your password : ")
# here we have declraed the strenght of the password and the remarks as none  
strength = 0
remarks = " "
# here we have have decleared all type of the counts and we need to check the password 
lower_count = upper_count = special_count = spaces_count = digits_count =  0 
# here we use the loop for the checking the how many and in which quantity characters are used by the user in his possword  
for char in list(password):
        # here checking the upper case of the alphabets 
    if char in string.ascii_uppercase:
        upper_count += 1
    elif char in string.ascii_lowercase:
        # here checking the lower case of the alphabets 
        lower_count += 1
    elif char in string.digits:
        # here checking the numeric characters of the numbers
        digits_count += 1
    elif char == " ":
        # here checking the spaces used by the user 
        spaces_count += 1
    else:
    # here checking the special case of the alphabets 
        special_count += 1
        
        
        # here checking that how many number of lower characters are used by the user 
if lower_count >= 1 : 
    strength += 1 
        # here checking that how many number of upper characters are used by the user 
if upper_count >= 1 :
    strength += 1 
        # here checking that how many number of special characters are used by the user 
if special_count >= 1 :
    strength += 1 
        # here checking that how many number of numeric characters are used by the user 
if digits_count >= 1 :
    strength += 1 
        # here checking that how many number of spaces characters are used by the user 
if spaces_count >= 1:
    strength += 1
            
 # here we are assigning the password its strenght according to the rules we determine and fullfilled by the user  
if strength == 1:
        remarks = "A Bad Password!"   
elif strength == 2:
        remarks = "Not a good Password!"       
elif strength == 3:
        remarks = "A Better Password!"                                          
elif strength == 4:
        remarks = "A Hard Password!"                           
elif strength == 5:
    remarks = "A Strong Password!"   
    
    #here we have write the all numbers of charactes used by the user and its count   
print(f" Your password contain : ")
print(f" {lower_count} : lower case characters")       
print(f" {upper_count} : upper case characters")       
print(f" {digits_count} : nummeric characters")       
print(f" {special_count} : special case characters")       
print(f" {spaces_count} : space characters")  


print(f"Your password strength is {strength}")
print(f"Review : {remarks}")     