lst=list()
while True:
    xx=input("Enter a number:")
    if xx == "done" : break
    try:
        x=int(xx)
    except:
           print("Invalid input")
           continue
    lst.append(x)

print("Maximum is", max(lst))
print("Minimum is", min(lst)) 
   