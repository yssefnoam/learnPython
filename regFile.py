import re

def main():
    readfile = open("regFile.txt", "r")
    for line in readfile:
        if re.search("(yo|ya)ss", line):
            print(line)
    readfile.close()


if __name__ == "__main__":
    main()