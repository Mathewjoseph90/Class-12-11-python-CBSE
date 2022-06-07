def assending(L):
    return L.sort()
def dessending(L):
    return L.sort(reverse = True)

L_org = []
n = int(input("Enter the limit for list elements :"))
for i in range(n):
    value = int(input("Enter the value :"))
    L_org.append(value)


print("The original list =", L_org)
print("The list after assending = ")
assending(L_org)
print("The list after dessending =")
dessending(L_org)