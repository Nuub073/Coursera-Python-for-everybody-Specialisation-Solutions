# Use the file name mbox-short.txt as the file name
count =0 
big = 0 
big =float(big)
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:" ):
        a = float(line[20:26])
        big = big+a
        count = count +1
print('Average spam confidence:', big/count)
