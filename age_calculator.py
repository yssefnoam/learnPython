#!/usr/bin/python3
import datetime
def main():
    bod = input("Enter your birth day: ")
    now = datetime.datetime.now().year
    lkj = now - int(bod)
    print("Your age is {}".format(lkj))
main()
