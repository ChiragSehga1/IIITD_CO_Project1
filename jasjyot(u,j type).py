def bin_to_int(x,y):#x=binary | y = s or u (signed or unsigned)
    if (y == 's'):
        if len(x) < 32:
            x = x[0]*(32-len(x)) + x
        x = list(x)
        if x[0] == '1':
            for i in range(32):
                if x[i] == '0':
                    x[i] = '1'
                else:
                    x[i] = '0'
            if x[-1] == '0':
                x[-1] = '1'
            else:
                i = 31
                while (x[i] == '1'):
                    x[i] = '0'
                    i -= 1
                x[i] = '1'
    else:
        x = '0'*(32-len(x)) + x
        list(x)
    out = 0
    for i in range(32):
        if x[i] == '1':
            out += 1*2**(31-i)
    print(x)
    if y == 's' and x[0] == '1':
        out *= -1
    return out
def signextension(x):
    if len(x) < 32:
        x = x[0]*(32-len(x)) + x
def Utype(x):
    imm=x[0:20]#loading top 20 bits of immediate value
    rd=x[20:25]#loading register value
    opcode=x[25:]#loading opcode
    upperimmvalue=imm+12*"0"#computing upperimmediate value
    value = bin_to_int(upperimmvalue,'s')#converting to integer
    if opcode=="0110111":#lui
        registers[rd]=value
    if opcode=="0010111":#auipc 
        registers[rd]=program_counter+value
def Jtype(x):
    rd=x[20:25]
    opcode=x[25:]
    imm=x[0]+x[12:20]+x[11]+x[1:11]#reading the immediate value with correct syntax
    registers[rd]=program_counter+4#storing return address in register
    b10=imm+"0"
    b10=bin_to_int(b10,'s')
    program_counter+=b10
    program_counter=program_counter//4
    
    
while stop == 0:
    line_to_execute = code[program_counter][0]
    type_of_intruction = code[program_counter][1]

    if type_of_intruction == "R":#AKSHAT
        pass # <=====================================================================================
    if type_of_intruction == "I":#AKSHAT
        pass # <=====================================================================================
    if type_of_intruction == "S":#CHIRAG
        pass # <=====================================================================================
    if type_of_intruction == "B":#(needs to break loop if "00000000000000000000000001100011" found) #CHIRAG
        pass # <=====================================================================================
    if type_of_intruction == "U":#JASJYOT(done)
        Utype(line_to_execute)
        pass # <=====================================================================================
    if type_of_intruction == "J":#JASJYOT
        Jtype(line_to_execute)
        pass # <=====================================================================================
    if type_of_intruction == "bonus":
        bonus_type(line_to_execute)
