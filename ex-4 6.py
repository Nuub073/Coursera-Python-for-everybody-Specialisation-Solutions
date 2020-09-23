hrs = input("Enter Hours: ")
rate = input("Enter rate: ")
x=input("Enter overtime hours: ")
ohrs=float(x)
def computepay(hrs, rate, ohrs):
    pay=int(hrs)*float(rate)
    if ohrs>0:
       opay=int(ohrs)*float(rate)*1.5  
       y=pay+opay
       return y
    else:
	     return pay
print("Pay", computepay(hrs, rate, ohrs))
