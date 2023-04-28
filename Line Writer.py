# Open a file 
file = open("mylife.txt", "w")

# Write lines
while True:
    line = input("Enter line: ")
    file.write(line + "\n")
    choice = input("Are there more lines? y/n : ")
    if choice == "n" :
        break
    