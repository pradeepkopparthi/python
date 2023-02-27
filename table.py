#to print nth table example:2table
n=int(input("enter the table(n):"))
step_count=int(input("enter the number of steps:"))
i=1
while i<=step_count:
    value=n*i
    print(str(n),'x',str(i),'=',value)
    i+=1
