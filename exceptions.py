#if the foo.txt file not exist = erro , that why we write the try-except statments

def main():
    try:
        readFile = open("foo.txt", "r")
        for line in readFile:
            print(line)
        readFile.close()
    except IOError:
        print("File not found")
main()