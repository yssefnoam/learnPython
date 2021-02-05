import re

def main():
    readfile = open("regFile.txt", "r")
    for line in readfile:
        if re.search("(ya|yo)ss", line):
            print(line)
        else:
            print("not thing found in line ==> " + line)
    readfile.close()


if __name__ == "__main__":main()