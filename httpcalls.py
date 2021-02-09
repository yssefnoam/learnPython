#!/usr/bin/python
import urllib.request, json


def main():
    data = urllib.request.urlopen("http://headers.jsontest.com/").read()
    r = json.loads(data.decode("utf-8"))
    print(r, type(r))


if __name__ == '__main__':
    main()
