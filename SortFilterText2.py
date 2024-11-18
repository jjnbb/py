fn = input("Enter file name: ")
if len(fn) < 1:
    fn = ""

fh = open(fn)

try:
    with open(fn) as file:
        c = 0

        for line in fh:
            if line.startswith("From:"):
                text = line.rstrip().split()

                if len(text) > 1:
                    print(text[1])
                    c += 1

        print("There were", c, "lines in the file with From as the first word")
except FileNotFoundError:
    print("File not found")