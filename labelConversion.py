"""The final hashmap will have '\n' character removed from end of lines, with all labels converted to a number as
diff=labelLineNum-currentLineNum, that is, the line of the label relative to the current line
Thus, to get to the label, we'll do currentLineNum + diff, reaching that label line"""

def readFile():
    """Reads code from file and store them in a numbered hashmap, as well as number of lines in program"""
    file=open(r"C:\Users\user\OneDrive\Desktop\Chirag_CO\Assembly.txt",'r')
    code=list(file.readlines())
    lineNumber=1
    numberedCode={}
    for line in code:
        numberedCode[lineNumber]=line[0:-1]
        lineNumber+=1
    return numberedCode,lineNumber-1

def BType(a):
    """checks if an instruction line 'a' is BType""""
    l=["beq " , "bne " , "bge " , "bgeu" , "blt " , "bltu"]
    if a[0:4] in l:
        return True
    return False

def JType(a):
    """checks if an instruction line 'a' is JType""""
    return a[0:3]=="jal"

def labelConvert():
    """Converts all labels in the numberedCode to line difference between current and label line, and returns a numbered hashmap of the same"""
    numberedCode,numberOfLines=readFile()
    labelConverted={}
    #making a dictionary while label converting
    for i in range(1,numberOfLines+1):
        start=numberedCode[i].find(':')+1
        if BType(numberedCode[i][start:]) or JType(numberedCode[i][start:]):
            currentLineNum=i
            label=numberedCode[i].split(',')[-1]
            for k,v in numberedCode.items():
                a=v.find(':')
                if label==v[0:a]:
                    diff=k-currentLineNum
                    break
            index=numberedCode[i].find(label)
            labelConverted[i]=numberedCode[i][0:index]+str(diff)
        else:
            labelConverted[i]=numberedCode[i]
    return labelConverted
