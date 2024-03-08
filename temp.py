def labelConvert(b,s1,s2,label):
    line=0
    found=False
    data=readFromTextFile()    #in readTextFile.py
    for i in data:
        line+=1
        if i in label:
            a=i.find(label)
            if i[a+len(label)]!=':':
                print_error("Error: missing ':' or label name matches a command. Check line ",b,s1,s2,label)
            else:
                found=True
                break
    return (b,s1,s2,line)
    
