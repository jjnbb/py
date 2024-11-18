fn = input("Enter file name: ")
fh = open(fn)

tf = 0.0
c = 0

for line in fh:
    if line.startswith(""): # Add conditional text for filter
        continue

    num = float(line.strip()[pos:pos]) # Change 'pos' with relevant start and end

    tf += num
    c += 1

avg = tf / c
print("Average:", avg)