# WAP to input a string and count the number of upper and lower case letters

str_1 = input("Enter the string :")
uppercase = 0
lowercase = 0
i = 0
while i < (len(str_1)):
    obj = str_1[i]
    if obj.isupper() == True:
        uppercase = uppercase + 1
    if obj.islower() == True:
        lowercase = lowercase + 1
print("The number of uppercase letter = ",uppercase)
print("The number of lowercase letters = ",lowercase)
