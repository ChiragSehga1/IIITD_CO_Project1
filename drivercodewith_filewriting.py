class InstructionError(Exception):
    def __init__(self,message):
        super().__init__(self.message)

class RegisterError(Exception):
    def __init__(self,message):
        self.message = message

class InstructionSyntaxError(Exception):
    def __init__(self,message):
        self.message = message

class VirtualHaltError(Exception):
    def __init__(self,message):
        self.message = message

class ImmediateError(Exception):
    def __init__(self,message):
        self.message = message


def twoscompliment(x , n):
    num = int(x)
    
    if (num > ((2**(n-1)) - 1) or num < -(2**(n-1))):
        raise ImmediateError(f"{num} is an invalid immediate value")
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


def code_for_a_single_line(x):
    instruction_types = { "R":["add" , "sub" , "sll" , "slt" , "sltu" , "xor" , "srl" , "or" , "and"] ,
                         "I":[ "lw" , "addi" , "sltiu" , "jalr"] , 
                         "S":["sw"] , 
                         "B":["beq" , "bne" , "blt" , "bge" , "bltu" , "bgeu"] , 
                         "U":["lui" , "auipc"] , 
                         "J":["jal"]}

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
                "t6" : "11111" , }


    #c holds the type of instruction in a single chacter string
    #y stores the instruction in string format
    Instruction = x.split(" ")[0]
    try:
        Values = x.split(" ")[1].split(",")
    except:
        raise InstructionError(f"{Instruction} operation is not defined")#Need to change later
    variables = ["r1","r2","r3","immediate value"] 
    instruction_not_defined = True#error handling start
    for a in instruction_types:
        for b in instruction_types[a]:
            if b == Instruction:
                InstructionType = a
                instruction_not_defined = False
                break
    if instruction_not_defined:
        raise InstructionError(f"{Instruction} operation is not defined")
    if Instruction not in ["lw","sw","lui","auipc","jal"]:
        if len(Values)!=3:#change 2
            raise InstructionSyntaxError(f"incorrect format for {Instruction} instruction")
        if InstructionType in ["B","I"]:
            for i in range(0,2):
                variables[i] = Values[i]
                if Values[i] not in registers:
                    raise RegisterError(f"{Values[i]} is not a vaild register")
            try:
                if InstructionType == "B":
                    immediate = twoscompliment(Values[2] , 13)
                else:
                    immediate = twoscompliment(Values[2] , 12)
                variables[3] = immediate
            except ValueError:
                raise ImmediateError(f"{Values[2]} is an invalid immmediate value")#

        else: 
            for i in range(0,3):
                variables[i] = Values[i]
                if Values[i] not in registers:
                    raise RegisterError(f"{Values[i]} is not a vaild register")                    

    else:
        if len(Values)!=2:#change 2
            raise InstructionSyntaxError(f"incorrect format for {Instruction} instruction")
        if Instruction in ["lw","sw"]:
            immediate = Values[1].split("(")[0]
            sr = (Values[1].split("(")[1])[0:-1]
            if (Values[0] not in registers):
                raise RegisterError(f"{Values[0]} is not a vaild register")
            if (sr not in registers):
                raise RegisterError(f"{sr} is not a vaild register")
            try:
                immediate = twoscompliment(immediate , 12)
            except ValueError:
                raise ImmediateError(f"{immediate} is an invalid immmediate value")
            variables[0] = Values[0]
            variables[1] = sr
            variables[3] = immediate
        else:
            if (Values[0] not in registers):
                raise RegisterError(f"{Values[0]} is not a vaild register")
            try:
                if InstructionType == "J":
                    immediate = twoscompliment(Values[1] , 21)
                else:
                    immediate = twoscompliment(Values[1] , 32)

            except ValueError:
                raise ImmediateError(f"{immediate} is an invalid immmediate value")

            variables[0] = Values[0]
            variables[3] = immediate#error handling end

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
            

        a = funct7 + " " + registers[variables[2]] + " " + registers[variables[1]] + " " + funct3 + " " + registers[variables[0]] + " " + opcode
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
        
        a = variables[3] + " " + registers[variables[1]] + " " + funct3 + " " + registers[variables[0]] + " " + opcode
        #print(a)
        return a
    
    if InstructionType == "S":
        opcode = "0100011"
        funct3 = "010"
        a = variables[3][:7] + " " + registers[variables[0]] + " " + registers[variables[1]] + " " + funct3 + " " + variables[3][-5:] + " " + opcode
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
        a = variables[3][0] + variables[3][2:8] + " " + registers[variables[1]] + " " + registers[variables[0]] + " " + funct3 + " " + variables[3][8:12] + variables[3][1] + " " + opcode
        #print(a)
        return a
        
    if InstructionType == "U":
        if Instruction == "lui":
            opcode = "0110111"
        else:
            opcode = "0010111"
        a = variables[3][:20] + " " + registers[variables[0]] + " " + opcode
        return a
        #print(a)
        
    if InstructionType == "J":
        opcode = "1101111"
        b = variables[3][0] + variables[3][10:20] + variables[3][9] + variables[3][1:9]
        a = b + " " + registers[variables[0]] + " " + opcode
        return a
        #print(a)
