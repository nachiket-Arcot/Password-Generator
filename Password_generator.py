# importing the modules
import random


#naming the charcaters
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = ",./<>?;:[]{}-=_+)(*&^%$'/\|"


length = 15
 

#Defining the characters variable
characters = lower_case + upper_case + numbers + symbols

# creating the Password                                                                                                                                                                        
password = "".join(random.sample(characters,length))
print(password)

#Storing the Password if answer to Question is Yes
Option_to_store_the_password = str(input("Would you like to store the password?(Yes or No): "))
if Option_to_store_the_password == ("Yes"):
    
    file_of_generated_passwords = open('Generated_Password.txt')
    file_of_generated_passwords.write("Here is the generated password:", password)
    file_of_generated_passwords.write()
    file_of_generated_passwords.close()

    print("Your Password is located in Generated_Passwords.txt")

else:
    pass






