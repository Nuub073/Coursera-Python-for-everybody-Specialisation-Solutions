hrs = input("Enter Hours: ")
rate = input("Enter rate: ")
#normal work Hours
pay=int(hrs)*float(rate)
#overtime
x=input("Enter overtime hours: ")
ohrs=float(x)
if ohrs>0:
   opay=int(ohrs)*float(rate)*1.5  
   print(pay+opay)  
else:
	 print(pay)
 