fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From "):#Yha tu compare kr rha h har line ki vo line from se shuru hoti mahi hoti ya hoti h, agar hoti h, tu use chordh deta h(skip kr deta h) aur bas unhi lines ko print krta h jo From: se shuru hoti h
        continue
   #or
   #if line.startswith("From:")#Yha tu sare txt mein se search kr rha h konsi line From: se shuru hoti h, aur bas unhi line ko print kr rha h, no comparison taking place, bs dhoondh rhe h yha ham
   #Dono ka result same h, 1 hi baat h, agar koi complicated code ni aata to bs "if" wala use kryo, "if not" nahi, bina baat ki matthapachchi chordh
    words=line.split()
    print(words[1]) 
    count += 1
        
print("There were", count, "lines in the file with From as the first word")
