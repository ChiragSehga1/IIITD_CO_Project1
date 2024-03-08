def readFromTextFile():
    f=open("Assembly.txt",'r')
    data=list(f.readlines())
    f.close()
    return data
