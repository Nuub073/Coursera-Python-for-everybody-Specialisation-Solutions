
maxy= -1
mini= None
while True:
      nom=input("Enter a number :")
      if nom=="done":
         break
      try:
         fnom=int(nom)
      except:
            print("Invalid input") 
            continue
      if mini is None :
         mini=fnom
      elif fnom < mini:
           mini = fnom
      elif fnom > maxy:
           maxy = fnom
      
   
print("Maximum is", maxy)
print("Minimum is", mini)


      
      