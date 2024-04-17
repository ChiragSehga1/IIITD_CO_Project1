import sys

def readFile(x):
    # Reads code from file and store them in a numbered hashmap, as well as number of lines in program
    file = open( x ,'r')
    binary = file.readlines()
    for i in range (len(binary)):
        binary[i] = binary[i].strip("\n")
    temp = binary
    binary = []
    for i in temp:
        if i != "":
            binary = binary + [i]
    dictionary = {}
    for i in range(0,(len(binary))):
        line = binary[i]
        opcode = line[-7:]
        inst_type = None
        if opcode == '0110011':
            inst_type = 'R'
        elif opcode in ['0000011','0010011','1100111']:
            inst_type = 'I'            
        elif opcode == '0100011':
            inst_type = 'S'
        elif opcode == '1100011':
            inst_type = 'B'
        elif opcode in ['0110111','0010111']:
            inst_type = 'U'
        elif opcode == '1101111':
            inst_type = 'J'
        elif opcode == '0000000':
            inst_type = 'bonus'
        dictionary[(i+1)*4] = [line,inst_type]

    return dictionary

def DtoH(decimal):
    #takes an integer in decimal and returns a converted string in hexadecimal
    hex=''
    rem={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
    while(decimal>0):
        hex+=rem[decimal%16]
        decimal=decimal//16
    return hex[-1:0:-1]+hex[0]

def BtoD(binary):
    #takes a binary in string and returns a converted integer in decimal
    dec=0
    for i in range(0,len(binary)):
        dec=dec+int(binary[-(i+1)])*(2**(i))
    return dec

def bin_to_int(x,y = 'u'):#x=binary | y = s or u (signed or unsigned)
    sign = 1 #remembers if binary is positive
    if (y == 's'):
        if len(x) < 32: #sign extends signed binary
            x = x[0]*(32-len(x)) + x
        x = list(x)
        if x[0] == '1': #converts negative binary to twos complement positive number
            sign = -1
            for i in range(32):#bit flip
                if x[i] == '0':
                    x[i] = '1'
                else:
                    x[i] = '0'
            if x[-1] == '0':#plus 1
                x[-1] = '1'
            else:
                i = 31
                while (x[i] == '1'):
                    x[i] = '0'
                    i -= 1
                x[i] = '1'
    else:#converts unsigned binary to twos compliment
        x = '0'*(32-len(x)) + x
        list(x)
    out = 0
    for i in range(32): #converts binary to integer
        if x[i] == '1':
            out += 1*2**(31-i)
    out *= sign #turns int negative if binary is negative
    return out

def twoscompliment(num, n = 32):
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


def unsigned(num,n=32):
    a = ""
    tempnum = num
    while tempnum != 0:
        a = str(tempnum % 2) + a
        tempnum = tempnum // 2
    a = (n - len(a))*"0" + a 
    return a

global registers
registers = { "00000" : 0 ,
              "00001" : 0  ,
              "00010" : 0 ,
              "00011" : 0  , 
              "00100" : 0  ,
              "00101" : 0  ,
              "00110" : 0  ,
              "00111" : 0  ,
              "01000" : 0  ,  
              "01001" : 0  ,
              "01010" : 0  , 
              "01011" : 0  , 
              "01100" : 0 , 
              "01101" : 0  , 
              "01110" : 0  ,
              "01111" : 0 , 
              "10000" : 0 , 
              "10001" : 0  , 
              "10010" : 0  , 
              "10011" : 0  , 
              "10100" : 0  , 
              "10101" : 0 , 
              "10110" : 0 , 
              "10111" : 0  , 
              "11000" : 0  , 
              "11001" : 0  , 
              "11010" : 0 , 
              "11011" : 0  , 
              "11100" : 0 , 
              "11101" : 0 , 
              "11110" : 0  , 
              "11111" : 0}
global stack
stack = []

global memory
memory = {"0x00010000" : 0,
          "0x00010004" : 0,
          "0x00010008" : 0, 
          "0x0001000c" : 0,
          "0x00010010" : 0,
          "0x00010014" : 0,
          "0x00010018" : 0, 
          "0x0001001c" : 0,
          "0x00010020" : 0,
          "0x00010024" : 0,
          "0x00010028" : 0, 
          "0x0001002c" : 0,
          "0x00010030" : 0,
          "0x00010034" : 0,
          "0x00010038" : 0, 
          "0x0001003c" : 0,
          "0x00010040" : 0,
          "0x00010044" : 0,
          "0x00010048" : 0, 
          "0x0001004c" : 0,
          "0x00010050" : 0,
          "0x00010054" : 0,
          "0x00010058" : 0, 
          "0x0001005c" : 0,
          "0x00010060" : 0,
          "0x00010064" : 0,
          "0x00010068" : 0, 
          "0x0001006c" : 0,
          "0x00010070" : 0,
          "0x00010074" : 0,
          "0x00010078" : 0, 
          "0x0001007c" : 0 }
 
global program_counter
program_counter = {1 : 4}

global stop
stop = {1 : 0}

global updated
updated = {1 : 0}


def bonus_type(line_to_execute):
    if (line_to_execute == "00000000000000000000000000000000"):
        stop[1] = 1
        return
    if (line_to_execute == "10000000000000000000000000000000"):
        for i in registers:
            registers[i] = 0
        return
    if (line_to_execute[0] == "0" and line_to_execute[17:20] == "111"):
        first = line_to_execute[12:17]
        second = line_to_execute[20:25]
        #reverse first and store in second
        pass # <=====================================================================================
    if (line_to_execute[0] == "1" and line_to_execute[17:20] == "111"):
        first = line_to_execute[7:12]
        second = line_to_execute[12:17]
        third = line_to_execute[20:25]
        #multiple first and second (ignore overflow) and store in third
        pass # <=====================================================================================

def Utype(x):
    imm = x[0:20] #loading top 20 bits of immediate value
    rd = x[20:25] #loading register value
    opcode = x[25:]#loading opcode
    upperimmvalue=imm+12*"0"#computing upperimmediate value
    value = bin_to_int(upperimmvalue,"s")#converting to integer
    if opcode=="0110111":#lui
        registers[rd] = value
    if opcode=="0010111":#auipc 
        registers[rd] = program_counter[1] + value
        
def Jtype(x):
    rd=x[20:25]
    opcode=x[25:]
    imm=x[0]+x[12:20]+x[11]+x[1:11]#reading the immediate value with correct syntax
    registers[rd] = program_counter[1] + 4 #storing return address in register
    b10=imm+"0"
    b10=bin_to_int(b10,"s")
    program_counter[1] += b10
    updated[1] = 1
    
def Btype(linetoexecute):
    if(line_to_execute=="00000000000000000000000001100011"):#check for virtual halt
        stop[1] = 1
        return
    rs1=line_to_execute[7:12]
    rs2=line_to_execute[12:17]
    funct3=line_to_execute[17:20]
    immediate=line_to_execute[0]+line_to_execute[24]+line_to_execute[1:7]+line_to_execute[20:24]+'0'
    offset=BtoD(immediate)
    #beq
    if (funct3=="000" and registers[rs1]==registers[rs2]):
        program_counter[1] +=offset
    #bne
    elif (funct3=="001" and registers[rs1]!=registers[rs2]):
        program_counter[1] +=offset
    #blt
    elif (funct3=="100" and registers[rs1]<registers[rs2]):
        program_counter[1] +=offset
    #bge
    elif (funct3=="101" and registers[rs1]>=registers[rs2]):
        program_counter[1] +=offset
    #bltu
    elif (funct3=="110" and abs(registers[rs1])<abs(registers[rs2])):
        program_counter[1] +=offset
    #bgeu
    elif (funct3=="111" and abs(registers[rs1])>=abs(registers[rs2])):
        program_counter[1] +=offset

def Stype(line_to_execute):
    immediate = line_to_execute[0:7]+line_to_execute[20:25]
    ra=line_to_execute[7:12] #r1
    sp=line_to_execute[12:17] #r2
    funct3=line_to_execute[17:20]
    imm=BtoD(immediate)
    Hex=DtoH(registers[sp]+imm)
    if((int(registers[sp])+imm)%4!=0):
        print("Error, memory address is not a multiple of 4")
    mem='0x000' + Hex
    memory[mem]=registers[ra]
    
def Rtype(line):
    rsd = line[-12:-7]
    rs1 = line[-20:-15]
    rs2 = line[-25:-20]
    func7 = line[0:7]
    func3 = line[-15:-12]
    if func7 == '0100000':
        registers[rsd] = registers[rs1] - registers[rs2]#sub
    elif func3 == '000':
        registers[rsd] = registers[rs1] + registers[rs2]#add
    elif func3 == '001':#left shift
        rs1 = twoscompliment(registers[rs1])
        rs2 = twoscompliment(registers[rs2])[-5::]
        shift = bin_to_int(rs2) * '0'
        new = (rs1 + shift)[-32::]
        registers[rsd] = bin_to_int(new,'s')
    elif func3 == '010':
        if registers[rs1] < registers[rs2]:#slt
            register[rsd] = 1
        else:
            register[rsd] = 0
    elif func3 == '011':
        if bin_to_int(twoscompliment(registers[rs1])) < bin_to_int(twoscompliment(registers[rs2])):#sltu
            register[rsd] = 1
        else:
            register[rsd] = 0
    elif func3 == '101':#right shift
        registers[rsd] = bin_to_int((bin_to_int((twoscompliment(registers[rs2])[-5::]))*('0') + (twoscompliment(registers[rs1])))[0:-5],'s')
    elif func3 == '110':#or
        registers[rsd] = registers[rs1] | registers[rs2]
    elif func3 == '111':#and
        registers[rsd] = registers[rs1] & registers[rs2]


def Itype(line):
    
    opcode = line[-7::]
    rsd = line[-12:-7]
    func3 = line[-15:-12]
    rs1 = line[-20:-15]
    imm = line[0:12]
    
    if opcode == '0000011':#lw
        Hex= '0x000' + DtoH(registers[rs1] + bin_to_int(imm,'s'))
        registers[rsd] = memory[Hex]
        
    elif opcode == '0010011':
        if func3 == '000':#addi
            registers[rsd] = registers[rs1] + bin_to_int(imm,'s')
            
        else:#sltiu
            if bin_to_int(twoscompliment(registers[rs1])) < bin_to_int(imm):
                registers[rsd] = 1
            else:
                register[rsd] = 0
    elif opcode == '1100111':#jalr
        registers[rd] = program_counter[1] + 4
        temp = registers[rs1] + bin_to_int(imm)#
        if temp % 2 != 0:#temp exists because in the cornell simulator, program counter just needs to be even for jalr instructions but if program_counter isn't divisible by 4 then it doesn't jump
            temp -= 1
        if temp % 4 == 0:
            program_counter[1] = temp
            updated[1] = 1
    
code = readFile("trial.txt")

    
while (stop[1] == 0) and (program_counter[1] in code) :
    line_to_execute = code[program_counter[1]][0]
    type_of_intruction = code[program_counter[1]][1]

    if type_of_intruction == "R":#AKSHAT
        Rtype(line_to_execute)
    elif type_of_intruction == "I":#AKSHAT
        Itype(line_to_execute)
    elif type_of_intruction == "S":#CHIRAG
        Stype(line_to_execute)
    elif type_of_intruction == "B":#CHIRAG
        Btype(line_to_execute)
    elif type_of_intruction == "U":#JASJYOT
        Utype(line_to_execute)
    elif type_of_intruction == "J":#JASJYOT
        Jtype(line_to_execute)
    elif type_of_intruction == "bonus":
        bonus_type(line_to_execute)
    if updated[1] == 1:
        updated[1] = 0
        print(program_counter[1])
        for i in registers:
            print (i , " : " , registers[i])
        continue
    print(program_counter[1])
    for i in registers:
        print (i , " : " , registers[i])
    program_counter[1] += 4
