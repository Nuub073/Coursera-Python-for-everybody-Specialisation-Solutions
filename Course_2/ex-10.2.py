fname = open(input("Enter file name:"))
counts = dict()
for line in fname:
     if not line.startswith("From "):
         continue
     #u can't use line.find("0") kyunki hrs range from 09-14 15 17 etc, to 0 find krne pr error milega(it will print out  empty space, doing - 1 from the found zero will Also not cuz har line mein zero ni h as said above), so u split each line, find the time of the time, and then split the time on the basis of the colon and take the hour fron that(best way to find something is to double split, better than find func remember that))
     word = line.split()
     time = word[5]
     time_split = time.split(":")
     hr = time_split[0]
     counts[hr]= counts.get(hr, 0) + 1
     
sorted_yes =(sorted( (k,v) for k, v in counts.items())) 
for k, v in sorted_yes:
    print(k, v)