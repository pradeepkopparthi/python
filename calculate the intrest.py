#program to calculate daily intrest
#for hundred rupes daily intrest is 3 rs
amount=float(input('amount taken for intrest='))
intrest=float(input('enter the intrest of 100 rs per a day='))
value=amount/100
per_day=value*intrest
no_of_days=int(input('enter the no of days to pay the intrest'))
total_amount=amount+(per_day*no_of_days)
print('totai amount with intrest is=')
print(total_amount)
