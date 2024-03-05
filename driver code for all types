def twoscompliment(x , n):
    num = int(x)
    
    if (num > ((2**(n-1)) - 1) or num < -(2**(n-1))):
        print("error")
    
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
    instruction_type = { "R":["add" , "sub" , "sll" , "slt" , "sltu" , "xor" , "srl" , "or" , "and"] ,
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

    y = x.split(" ")[0]
    for a in instruction_type:
        for b in instruction_type[a]:
            if b == y:
                c = a
                break
                
    #c holds the type of instruction in a single chacter string
    #y stores the instruction in string format
    
    if c == "R":
        t = x.split(" ")[1].split(",")
        if y == "sub":
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
        funct3 = funct3_dict[y]
        

        a = funct7 + " " + registers[t[2]] + " " + registers[t[1]] + " " + funct3 + " " + registers[t[0]] + " " + opcode
        #print(a)
        return a
    
    if c == "I":
        t = x.split(" ")[1].split(",")
        if y == "lw":
            opcode = "0000011"
        elif y == "jalr":
            opcode = "1100111"
        else:
            opcode = "0010011"
        
        if y == "lw":
            funct3 = "010"
        elif y == "sltiu":
            funct3 = "011"
        else:
            funct3 = "000"        
        
        immediate = twoscompliment(t[2] , 12)
        
        a = immediate + " " + registers[t[1]] + " " + funct3 + " " + registers[t[0]] + " " + opcode
        #print(a)
        return a
    
    if c == "S":
        t = x.split(" ")[1].split(",")
        opcode = "0100011"
        funct3 = "010"
        immediate = twoscompliment(t[2] , 12)
        a = immediate[:7] + " " + registers[t[0]] + " " + registers[t[1]] + " " + funct3 + " " + immediate[-5:] + " " + opcode
        #print(a)
        return a
        
    if c == "B":
        t = x.split(" ")[1].split(",")
        opcode = "1100011"
        funct3_dict = {
            "beq" : "000",
            "bne" : "001",
            "blt" : "100",
            "bge" : "101",
            "bltu" : "110",
            "bgeu" : "111"
        }
        funct3 = funct3_dict[y]
        immediate = twoscompliment(t[2] , 13)
        a = immediate[0] + immediate[2:8] + " " + registers[t[1]] + " " + registers[t[0]] + " " + funct3 + " " + immediate[8:12] + immediate[1] + " " + opcode
        #print(a)
        return a
        
    if c == "U":
        t = x.split(" ")[1].split(",")
        if y == "lui":
            opcode = "0110111"
        else:
            opcode = "0010111"
        immediate = twoscompliment(t[1] , 32)   
        a = immediate[:20] + " " + registers[t[0]] + " " + opcode
        return a
        #print(a)
        
    if c == "J":
        t = x.split(" ")[1].split(",")
        opcode = "0010111"
        immediate = twoscompliment(t[1] , 21)
        b = immediate[0] + immediate[10:20] + immediate[9] + immediate[1:9]
        a = b + " " + registers[t[0]] + " " + opcode
        return a
        #print(a)
    
        
