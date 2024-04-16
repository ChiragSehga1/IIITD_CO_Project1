def bin_to_int(b):
    return int(b, 2)
def signextension(x):
    if len(x) < 32:
        x = x[0]*(32-len(x)) + x
def Utype(x):
    imm=x[0:20]
    rd=x[20:25]
    opcode=x[25:]
    upperimmvalue=imm+12*"0"
    value = int(upperimmvalue, 2)
    if opcode=="0110111":#lui
        registers[rd]=value
    if opcode=="0010111":#auipc 
        registers[rd]=program_counter+value
def Jtype(x):
    rd=x[20:25]
    opcode=x[25:]
    imm=x[0]+x[12:20]+x[11]+x[1:11]
    registers[rd]=program_counter+4
    b10=imm+"0"
    b10=int(b10,2)
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
