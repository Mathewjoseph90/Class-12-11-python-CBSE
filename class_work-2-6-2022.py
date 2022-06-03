def min_max(L):
    print("The max element of the list", max(L))
    print("the min element of the list", min(L))

def sum_all(L):
    return print(sum(L))

def reverse_list(L):
    L.reverse()
    return print(L)

def swap(L):

    for i in range(len(L)-1):
       temp = L[i+1]
       L[i+1] = L[i]
       L[i] = temp

    return print("The list after swap",L)
limit = int(input("Enter the number of elements in the list :"))
list  = []
i = 0
while i < limit :
    values = int(input("Enter the elements of the list :"))
    list.append(values)
    i += 1
print("The created List = ",list)

dis = 'y'
while dis == 'y':
    print(" (1) To find the max and min of the list \n (2) To find the sum of all the elements of the list \n"
    " (3) To reverse the list \n (4) Swap the elements")
    choice_variable = int(input(":"))

    if choice_variable == 1:
        min_max(list)
    elif choice_variable == 2:
        sum_all(list)
    elif choice_variable == 3:
        reverse_list(list)
    elif choice_variable == 4:
        swap(list)
    else:
        print("Enter a valid number")

    dis = input("do you wish to continue y/n :")
    
