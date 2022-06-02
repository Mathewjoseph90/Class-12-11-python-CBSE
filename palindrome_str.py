str = input("Enter the string to be checked :")
i = 0
j = -1
flag = 0
while i < len(str):
    if str[i] != str[j]:
        print("not a  palendrom")
        flag = 1
        break
    else:
        j += -1
    i+=1
if flag == 0 :
    print("palendrom")