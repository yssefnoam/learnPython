#!$(test)
def display():
    print("Welcome from function")
def sumNumbers(n1, n2):
    z = n1 + n2
    print ("z = {}".format(z))

def sumNumbers2(n1, n2):
    return n1 + n2
def main():
    #display()
    #sumNumbers(3, 5)
    print(sumNumbers2(4,6))

main()
