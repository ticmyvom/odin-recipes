filename = "input.txt"

with open(filename) as f:
    content = f.readlines()

# Add the open and close list tags to nonempty lines
for line in content:
    line = line.strip()
    # If the length of the line is 0 after stripping spaces then it's an empty line to begin with -> skip
    if len(line) != 0: 
        print("<li>" + line + "</li>")
   