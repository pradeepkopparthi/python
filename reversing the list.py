#to reverse a list with out using built in functions
list=[]
n=int(input("enter the number of elements in the list:"))
for i in range(n):
    list.append(int(input("enter element:")))
print(list)
x=n-1
while list[x] in list:
    print(list[x])
    x=x-1
    if x==-1:
        break
