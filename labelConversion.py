"""
The last function is all that needs to run, which will make 2 major changes:

1. The final hashmap will have '\n' character removed from end of lines, with all labels converted to a number as
diff=labelLineNum-currentLineNum, that is, the line of the label relative to the current line
Thus, to get to the label, we'll do currentLineNum + diff, reaching that label line

2. All label names will be removed. Lines that contain only label names will become empty lines (instead of being removed) 
in order to preserve line number order. Lines that have instructions after the label name will work as is, with the label name
removed from the beginning.
"""

def readFile():
    """Reads code from file and store them in a numbered hashmap, as well as number of lines in program"""
    file=open(r"C:\Users\gaurm\OneDrive\Desktop\Assembly.txt",'r')
    code=list(file.readlines())
    lineNumber=1
    numberedCode={}
    if code[-1][-1]!='n':
        code[-1]=code[-1]+'\n'
    for line in code:
        numberedCode[lineNumber]=line[0:-1].strip()
        lineNumber+=1
    return numberedCode,lineNumber-1

def BType(a):
    """checks if an instruction line 'a' is BType"""
    l=["beq " , "bne " , "bge " , "bgeu" , "blt " , "bltu"]
    if a[0:4] in l:
        return True
    return False

def JType(a):
    """checks if an instruction line 'a' is JType"""
    return a[0:3]=="jal"

def labelConvert():
    """Converts all labels in the numberedCode to line difference between current and label line, and returns a numbered hashmap of the same"""
    numberedCode,numberOfLines=readFile()
    #making a dictionary while label converting
    for i in range(1,numberOfLines+1):
        start=numberedCode[i].find(':')+1
        if BType(numberedCode[i][start:]) or JType(numberedCode[i][start:]):
            label = numberedCode[i].split(',')[-1]
            if (label.isdigit()) or (label[1:].isdigit() and label[0] == "-"):
                break
                
            foundLabel=False
            currentLineNum=i

            for k,v in numberedCode.items():
                a=v.find(':')
                if label==v[0:a]:
                    diff=k-currentLineNum
                    foundLabel=True
                    break
            if foundLabel:
                index=numberedCode[i].find(label)
            else:
                print("Error: Label name \'",label,"\' not found") #change this to error format
                return {}
            numberedCode[i]=numberedCode[i][0:index]+str(diff)
    return numberedCode

def removeAllLabels():
    labelConverted=labelConvert()
    for k,v in labelConverted.items():
        a=v.find(':')+1
        if v[a] == " ":
            a = a + 1
            labelConverted[k]=v[a:]
        else:
            labelConverted[k]=v[a:]
        #print(k,v,a)
    return labelConverted
