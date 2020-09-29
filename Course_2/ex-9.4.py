
hey = input("Enter file name:")
fname = open(hey)
count = dict()
for line in fname:
    if not line.startswith('From '):
        continue
    
    words = line.split()
    email = words[1]
    count[email] = count.get(email, 0) +1 
    
maxcount = None
maxemail = None

for mail, counts in count.items():
    if maxcount is None or counts > maxcount :
         maxcount = counts
         maxemail = mail
         
print(maxemail, maxcount)