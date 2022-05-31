# Built-in fuctions of string according to class 12th Preeti Arora

def string():
# Using time module to calculate the time taken to run a program
    import time 
    start = time.time()

# Inputing data from the user
    test_str = input("enter the required string :")

    print('-'*50)

# .isalpha() to check if the string only contains alphabets without whitespace or digits
    print('alphabet = ', test_str.isalpha())

    print('-'*50)

# .isdigit() is used to check if the string only contains digits
    print('digit = ', test_str.isdigit())

    print('-'*50)

# len() is used to determine the number of charactors
    print('no of charectors = ', len(test_str))

    print('-'*50)

# .lower() is used to lowercase the whole string
    print('the string in lowercase = ', test_str.lower())

    print('-'*50)

# .upper() is used to upercase the whole string 
    print('The string in uppercase =', test_str.upper())

    print('-'*50)

# .islower() is used to check whether the entire string is in lowercase 
    print('whether all the charectors are in lowercase = ', test_str.islower())

    print('-'*50)

# .isupper() is used to check whether the entire string is in uppercase 
    print('whether all the charectors are in lowercase = ', test_str.isupper())

    print('-'*50)

# dis_1 = decision variable - 1 used for replace()
    dis_1 = int(input("Do you want to replace any charector from the string (1/0) :"))
    if dis_1 == 1:  
        replace_ = input("enter the charector to be replaced :")
        replace_2 = input("enter the charector to be replaced with :")
        print("the string after replacement =", test_str.replace(replace_, replace_2))  # <original_string>.replace("the charactor to be replaced ","the charactor to replace") 
                                                                                        # replaces all occurrence of the old string with new string 

    print('-'*50)
 
# dis_2 = decision variable - 2 used for find()   
    dis_2 = int(input("Do you desire to find any charactor (1/0) :"))                                 
    if dis_2 == 1:
        find_ = input("Enter charector to find :")
        print('the charector was found in index = ', test_str.find(find_))  # <original_string>.find("The charactor to find") is used to search the first 
                                                                            # occurence of the substring in the given string 

    print('-'*50)

# .lstrip() is used to remove all the whitespaces from the left
    print('string after removing all the space from left = ', test_str.lstrip())

    print('-'*50)

# .rstrip() is used to remove all the whitespaces from the right 
    print('string after removing all the space from right = ', test_str.rstrip())

    print('-'*50)

# .isspace() checks if the string has only whitespaces 
    print('Does the string contain only space = ', test_str.isspace())

    print('-'*50)

# .istitle() checks if the string is a Title ie. every words starts with a capital letter
    print("Is the string a Title =", test_str.istitle())

    print('-'*50)

# dis_3 = decision variable - 3 used for join()
    dis_3 = int(input("Do you wish to join the string using a sequence (1/0):"))
    if dis_3 == 1:
        join_ = input("Enter the sequence to use as a separator :")
        print("String after separation =", join_.join(test_str))  # <separator>.join(<original_string>) is used to return a string 
                                                                  # which the string elements have been joined by a string separator 

    print('-'*50)

# .swapcase() is used to swap the upercase to lowercase and vice versa
    print("string after swaping all the keys =", test_str.swapcase())

    print('-'*50)

# dis_4 = decision variable - 4 used for partition()
    dis_4 = int(input("Do you wish to use partition method (1/0) :"))
    if dis_4 == 1:
        partition_ = input("enter the Separator :")
        print("The string after partition =", test_str.partition(partition_)) # <original_string>.partition(<separator>) is used to split the given string using
                                                                               # the specified sepator and returns a tuple with three parts

    print('-'*50)

# dis_5 = decision variable - 5 is used for endwith()                                                        
    dis_5 = int(input("Do you wish to use endswith (1/0) :"))               
    if dis_5 == 1:
        endswith_ = input("Enter substring :")
        print("Does the string end with the substring =", test_str.endswith(endswith_)) # <original_string>.endswith(<the substring>) returns True if the given strings
                                                                                        # ends with specified substring

    print('-'*50)

# dis_6 = decision variable - 6 is used for startwith()
    dis_6 = int(input("Do you wish to use startwith method (1/0) :"))
    if dis_6 == 1:
        startwith_ = input("Enter the substring :")
        print("Does the string startswith a substring =", test_str.startswith(startwith_)) # <original_string>.stratswith("the substring") returns True if the given strings
                                                                                           # starts with specified substring   

    print('-'*50)

    end = time.time()
    print(f"The time taken ton run the program {end - start}") # prints the time taken to run the program
    print(__name__)
string()