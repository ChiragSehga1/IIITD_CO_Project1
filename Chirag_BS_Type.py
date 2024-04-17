global registers
registers = { "00000" : 0 ,
              "00001" : 9  ,
              "00010" : 7 ,
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
              "01101" : 7  , 
              "01110" : 0  ,
              "01111" : 4 , 
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
program_counter= 0
global stop
stop = 0

"""copy paste lines 81 to 96 to general function definitions 
If conflicted
DtoH is called in line 130 only (and in Akshat's code)
BtoD is called in lines 106 and 131
"""
def DtoH(decimal):
    #takes an integer in decimal and returns a converted string in hexadecimal
    hex=''
    rem={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
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


type_of_instruction='S'
line_to_execute="00000010000100010010000000100011"
"""
I know this would've been better in a function but my global seems 
to stop working when used inside of a function, so yeah
"""
#copy paste line till line 132 to B-Type instruction condition
for i in range(0,1): #only done for ease of testing of virutual halt, break
    if (type_of_instruction=='B'):
        if(line_to_execute=="00000000000000000000000001100011"):#check for virtual halt
          stop=1  
          break #comment out 103,104 for testing
        rs1=line_to_execute[7:12]
        rs2=line_to_execute[12:17]
        funct3=line_to_execute[17:20]
        immediate=line_to_execute[0]+line_to_execute[24]+line_to_execute[1:7]+line_to_execute[20:24]+'0'
        offset=BtoD(immediate)
        #beq
        if (funct3=="000" and registers[rs1]==registers[rs2]):
            program_counter+=offset
        #bne
        elif (funct3=="001" and registers[rs1]!=registers[rs2]):
            program_counter+=offset
        #blt
        elif (funct3=="100" and registers[rs1]<registers[rs2]):
            program_counter+=offset
        #bge
        elif (funct3=="101" and registers[rs1]>=registers[rs2]):
            program_counter+=offset
        #bltu
        elif (funct3=="110" and abs(registers[rs1])<abs(registers[rs2])):
            program_counter+=offset
        #bgeu
        elif (funct3=="111" and abs(registers[rs1])>=abs(registers[rs2])):
            program_counter+=offset

#copy paste till eof to S-Type instruction condition
if (type_of_instruction=='S'):
    immediate=line_to_execute[0:7]+line_to_execute[20:25]
    ra=line_to_execute[7:12] #r1
    sp=line_to_execute[12:17] #r2
    funct3=line_to_execute[17:20]
    imm=BtoD(immediate)
    Hex=DtoH(registers[ra]+imm)
    if((int(registers[ra])+imm)%4!=0):
        print("Error, memory address is not a multiple of 4")
    mem='0x000100'+Hex
    memory[mem]=registers[sp]

    
