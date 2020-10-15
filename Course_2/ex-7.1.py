# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
hh= fh.read()
hhh=hh.rstrip()
print(hhh.upper())
