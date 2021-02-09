def main():
    file=open("foo.txt", "w")
    file.write("line1")
    file.write("\nline2")
    file.write("\nline3")
    file.write("\nline4")
    file.write("\nline5")
    file.write("\nline6")
    file.close()
    readFile = open("foo.txt", "r")
    for line in readFile:
        print(line)
    readFile.close()


main()