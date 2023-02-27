a=int(input('enter maths marks'))
b=int(input('enter python marks'))
c=int(input('enter chemistry marks'))
d=int(input('enter physics marks'))
sum=a+b+c+d
value=sum/4
print(str(value)+"%")
if value>=90 and value<=100:
    print('grade is A')
elif value>=80 and value<90:
    print('grade is B')
elif value>=70 and value<80:
    print('grade is C')
elif value>=60 and value<70:
    print('grade is D')
elif value>=50 and value<60:
    print('grade is E,just pass')
else:
    print('grade is F,he failed')
    
