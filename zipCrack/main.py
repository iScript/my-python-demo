# encoding:utf-8
import zipfile
import os


def extractFile(zFile,password):
    try:
        zFile.extractall(path = os.getcwd(), pwd = password.encode('utf-8'))
        return password
    except:
        pass


def main():
    zFile = zipfile.ZipFile('test.zip')
    passFile = open('dict.txt')

    for line in passFile.readlines():
        password = line.strip("\n")     #移除 \n

        guess = extractFile(zFile,password)
        if guess:
            print("password = ",password)
        else:
            continue
            #print("cannot")
            #return

if __name__ == "__main__":
    main()
