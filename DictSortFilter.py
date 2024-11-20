fn = input("Enter file name: ")
if len(fn) < 1:
    fn = "sample.txt"

try:
    with open(fn) as file:
        d = dict()
        # count occurrences of each email
        for line in file:
            if line.startswith("From "):
                text = line.rstrip().split()

                if len(text) > 1:
                    email = text[1]
                    d[email] = d.get(email, 0) + 1
        # find the most common email
        common = None
        c = 0

        for email, o in d.items():
            if o > c:
                common = email
                c = o

        print(common, c)
except FileNotFoundError:
    print("File not found")