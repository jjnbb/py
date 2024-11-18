fn = input("Enter file name: ")
fh = open(fn)

el = list()

for line in fh:
    words = line.rstrip().split()

    for word in words:
        if word not in el:
            el.append(word)

el.sort()
print(el)