fname = input("Enter file name: ")
if len(fname) < 1: fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    wrd = line.split()
    if len(wrd) < 3 or wrd[0] != 'From':
        continue
    print(wrd[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")
