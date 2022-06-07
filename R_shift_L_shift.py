def l_shift(l):
    temp = l[len(l)-1]
    l.remove(l[len(l)-1])
    l.insert(0,temp)
    return l
def r_shift(l):
    temp = l[0]
    l.remove(l[0])
    l.insert(-1,temp)
    return l

limit = int(input("Enter the limit of the elements in the list :"))
i = 0
L = []
while i < limit :
    value = int(input("Enter the value:"))
    L.append(value)
    i+= 1
L1 = L.copy()
L2 = L.copy()
print("The original list :")
print(L)
print("The list after L_shift :")
print(l_shift(L1))
print("The list after R_shift :")
print(r_shift(L2))