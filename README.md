# max and min in a list
list=[]
n=int(input('enter the no of elements='))
for i in range(n):
    list.append(int(input('enter elements:')))
print(list)
minimum=list[0]
for element in list:
        if minimum>element:
            minimum=element
print('minimum number in list is:')            
print(minimum)
maximum=list[0]
for element in list:
        if maximum<element:
            maximum=element
print('maximum number in list is:')            
print(maximum)
    
