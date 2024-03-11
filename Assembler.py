import sys

def readFile(x):
    """Reads code from file and store them in a numbered hashmap, as well as number of lines in program"""
    file = open(x,'r')
    code=list(file.readlines())
    lineNumber=1
    numberedCode={}
    if code[-1][-1]!='n':
        code[-1]=code[-1]+'\n'
    for line in code:
        if line == "\n":
            continue
        numberedCode[lineNumber]=line[0:-1].strip()
        lineNumber+=1
    lineNumber -= 1
    while numberedCode[lineNumber] == "":
        del numberedCode[lineNumber]
        lineNumber -= 1
    return numberedCode,lineNumber

def BType(a):
    """checks if an instruction line 'a' is BType"""
    l=["beq " , "bne " , "bge " , "bgeu" , "blt " , "bltu"]
    if a[0:4] in l:
        return True
    return False

def JType(a):
    """checks if an instruction line 'a' is JType"""
    return a[0:3]=="jal"

def labelConvert(x):
    """Converts all labels in the numberedCode to line difference between current and label line, and returns a numbered hashmap of the same"""
    numberedCode,numberOfLines=readFile(x)
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
                    diff= 4*(k-currentLineNum) #take care of this
                    foundLabel=True
                    break
            if foundLabel:
                index = numberedCode[i].find(label)
            else:
                return (f"LabelError: Label not found for label {label} referenced at line {currentLineNum}")
            numberedCode[i]=numberedCode[i][0:index]+str(diff)
    return numberedCode

def removeAllLabels(x):
    labelConverted=labelConvert(x)
    for k,v in labelConverted.items():
        a=v.find(':')+1
        if v[a] == " ":
            a = a + 1
            labelConverted[k]=v[a:]
        else:
            labelConverted[k]=v[a:]
        #print(k,v,a)
    return labelConverted

def twoscompliment(x , n):
    num = int(x)
    
    if (num > ((2**(n-1)) - 1) or num < -(2**(n-1))):
        return "ERROR"
    else:
        if num >= 0:
            a = ""
            tempnum = num
            while tempnum != 0:
                a = str(tempnum % 2) + a
                tempnum = tempnum // 2
            a = (n - len(a))*"0" + a 
            return a
        
        else:
            a = ""
            tempnum = (num*(-1)) - 1
            while tempnum != 0:
                a = str(tempnum % 2) + a
                tempnum = tempnum // 2
            a = str(int(n*"1") - int(a))
            a = (n - len(a))*"0" + a
            return a            


def code_for_a_single_line(x , y):
    
    if x == "":
        return ""
    
    instruction_types = { "R":["add" , "sub" , "sll" , "slt" , "sltu" , "xor" , "srl" , "or" , "and"] ,
                         "I":[ "lw" , "addi" , "sltiu" , "jalr"] , 
                         "S":["sw"] , 
                         "B":["beq" , "bne" , "blt" , "bge" , "bltu" , "bgeu"] , 
                         "U":["lui" , "auipc"] , 
                         "J":["jal"],
                        "bonus" : ["mul" , "rst" , "halt" , "rvrs"]}
    
    #assumed "halt" in machine code is "00000000000000000000000000000000"
    #assumed "rst" in machine code is "10000000000000000000000000000000"
    #assumed "rvrs rd,rs" in machine code is "000000000000[rs1]111[rd]0000000"
    #assumed "mul rd,rs1,rs2" in machine code is "1000000[rs2][rs1]111[rd]0000000"

    registers = { "zero" : "00000" ,
                "ra" : "00001" ,
                "sp" : "00010" ,
                "gp" : "00011" , 
                "tp" : "00100" ,
                "t0" : "00101" ,
                "t1" : "00110" ,
                "t2" : "00111" ,
                "s0" : "01000" , 
                "fp" : "01000" , 
                "s1" : "01001" ,
                "a0" : "01010" , 
                "a1" : "01011" , 
                "a2" : "01100" , 
                "a3" : "01101" , 
                "a4" : "01110" ,
                "a5" : "01111" , 
                "a6" : "10000" , 
                "a7" : "10001" , 
                "s2" : "10010" , 
                "s3" : "10011" , 
                "s4" : "10100" , 
                "s5" : "10101" , 
                "s6" : "10110" , 
                "s7" : "10111" , 
                "s8" : "11000" , 
                "s9" : "11001" , 
                "s10" : "11010" , 
                "s11" : "11011" , 
                "t3" : "11100" , 
                "t4" : "11101" , 
                "t5" : "11110" , 
                "t6" : "11111"  }
    
    if x == "halt":
        return "00000000000000000000000000000000"
    
    if x == "rst":
        return "10000000000000000000000000000000"
                

    Instruction = x.split(" ")[0]
    try:
        Values = x.split(" ")[1].split(",")
    except:
        return (f"InstructionError: {Instruction} operation is not defined at line {y}") #Need to change later
    variables = ["r1","r2","r3","immediate value"] 
    instruction_not_defined = True #error handling start
    for a in instruction_types:
        for b in instruction_types[a]:
            if b == Instruction:
                InstructionType = a
                instruction_not_defined = False
                break
    if instruction_not_defined:
        return (f"InstructionError: {Instruction} operation is not defined at line {y}")
    if Instruction not in ["lw","sw","lui","auipc","jal","rvrs"]:
        if len(Values)!=3:#change 2
            return (f"InstructionSyntaxError: incorrect format for {Instruction} instruction at line {y}")
        if InstructionType in ["B","I"]:
            for i in range(0,2):
                variables[i] = Values[i]
                if Values[i] not in registers:
                    return (f"RegisterError: {Values[i]} is not a vaild register at line {y}")
            try:
                if InstructionType == "B":
                    immediate = twoscompliment(Values[2] , 13)
                    if immediate == "ERROR":
                        return (f"ImmediateError: {Values[2]} is an invalid immediate value at line {y}")
                        ##################################################################
                else:
                    immediate = twoscompliment(Values[2] , 12)
                    if immediate == "ERROR":
                        return (f"ImmediateError: {Values[2]} is an invalid immediate value at line {y}")
                        ################################################################
                variables[3] = immediate
            except ValueError:
                return (f"ImmediateError: {Values[2]} is an invalid immmediate value at line {y}")#

        else: 
            for i in range(0,3):
                variables[i] = Values[i]
                if Values[i] not in registers:
                    return (f"RegisterError: {Values[i]} is not a vaild register at line {y}")                    

    else:
        if len(Values)!=2:#change 2
            return (f"InstructionSyntaxError: incorrect format for {Instruction} instruction at line {y}")
        if Instruction in ["lw","sw"]:
            immediate = Values[1].split("(")[0]
            sr = (Values[1].split("(")[1])[0:-1]
            if (Values[0] not in registers):
                return (f"RegisterError: {Values[0]} is not a vaild register at line {y}")
            if (sr not in registers):
                return (f"RegisterError: {sr} is not a vaild register at line {y}")
            try:
                immediate = twoscompliment(immediate , 12)
                if immediate == "ERROR":
                    return (f"ImmediateError: {immediate} is an invalid immediate value at line {y}")
            except ValueError:
                return (f"ImmediateError: {immediate} is an invalid immmediate value at line {y}")
            variables[0] = Values[0]
            variables[1] = sr
            
            variables[3] = immediate
        else:
            if (Values[0] not in registers):
                return (f"RegisterError: {Values[0]} is not a vaild register at line {y}")
            if Instruction == "rvrs":
                variables[1] = Values[1]
            else:
                try:
                    if InstructionType == "J":
                        immediate = twoscompliment(Values[1] , 21)
                        if immediate == "ERROR":
                            return (f"ImmediateError: {Values[1]} is an invalid immediate value at line {y}")
                    else:
                        immediate = twoscompliment(Values[1] , 32)
                        if immediate == "ERROR":
                            return (f"ImmediateError: {Values[1]} is an invalid immediate value at line {y}")
                    variables[3] = immediate #error handling end
                except:
                    return (f"ImmediateError: {immediate} is an invalid immmediate value at line {y}")
            variables[0] = Values[0] #error handling end

    if InstructionType == "R":        
        if  Instruction == "sub":
            funct7 = "0100000"
        else:
            funct7 = "0000000"
            
        opcode = "0110011"
            
        funct3_dict = {"add" : "000" ,
                      "sub" : "000" ,
                      "sll" : "001" ,
                      "slt" : "010" ,
                      "sltu" : "011" ,
                      "xor" : "100" , 
                      "srl" : "101" , 
                      "or" : "110" ,
                      "and" : "111"}
        funct3 = funct3_dict[Instruction]
            

        a = funct7  + registers[variables[2]]  + registers[variables[1]] + funct3 + registers[variables[0]] + opcode
        #print(a)
        return a
    
    if InstructionType == "I":        

        if Instruction == "lw":
            opcode = "0000011"
        elif Instruction == "jalr":
            opcode = "1100111"
        else:
            opcode = "0010011"
        
        if Instruction == "lw":
            funct3 = "010"
        elif Instruction == "sltiu":
            funct3 = "011"
        else:
            funct3 = "000"        
        
        a = variables[3] + registers[variables[1]] + funct3 + registers[variables[0]] + opcode
        #print(a)
        return a
    
    if InstructionType == "S":
        opcode = "0100011"
        funct3 = "010"
        a = variables[3][:7] +  registers[variables[0]] +  registers[variables[1]]  + funct3  + variables[3][-5:] + opcode
        #print(a)
        return a
        
    if InstructionType == "B":
        opcode = "1100011"
        funct3_dict = {
            "beq" : "000",
            "bne" : "001",
            "blt" : "100",
            "bge" : "101",
            "bltu" : "110",
            "bgeu" : "111"
        }
        funct3 = funct3_dict[Instruction]
        a = variables[3][0] + variables[3][2:8]  + registers[variables[1]] + registers[variables[0]]  + funct3 + variables[3][8:12] + variables[3][1]  + opcode
        #print(a)
        return a
        
    if InstructionType == "U":
        if Instruction == "lui":
            opcode = "0110111"
        else:
            opcode = "0010111"
        a = variables[3][:20] + registers[variables[0]]  + opcode
        return a
        #print(a)
        
    if InstructionType == "J":
        opcode = "1101111"
        b = variables[3][0] + variables[3][10:20] + variables[3][9] + variables[3][1:9]
        a = b + registers[variables[0]]  + opcode
        return a
        #print(a)

    if "mul" in x:
        return "1000000" + registers[variables[2]] + registers[variables[1]] + "111" + registers[variables[0]] + "0000000"

    if "rvrs" in x:
        return "000000000000" + registers[variables[1]] + "111" + registers[variables[0]] + "0000000"

count = 1

input_file = str(sys.argv[1])
output_file = str(sys.argv[2])

LOC = removeAllLabels(input_file)
list_of_LOC = []

while count in LOC:
    list_of_LOC = list_of_LOC + [LOC[count]]
    count += 1

    

if "beq zero,zero,0" in list_of_LOC:
    if list_of_LOC[-1] != "beq zero,zero,0":
        return (f"LastLineError: Virtual Halt is not the last line of the code (at line {y} instead)")
else:
    return ("VirtualHaltError: Virtual Halt is not present")
    

final_code = ""

count = 1
for codeline in list_of_LOC:
    code_of_a_line = code_for_a_single_line(codeline , count)
    if "Error" in code_of_a_line:
        final_code = code_of_a_line + " "
        break
    count += 1
    if code_of_a_line == "":
        continue
    else:
        final_code = final_code + code_of_a_line + "\n"
final_code = final_code[:-1]


file = open(output_file,'w')
file.write(final_code)

file.close()
