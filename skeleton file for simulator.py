#assumed "halt" in machine code is "00000000000000000000000000000000"
#assumed "rst" in machine code is "10000000000000000000000000000000"
#assumed "rvrs rd,rs" in machine code is "000000000000[rs1]111[rd]0000000"
#assumed "mul rd,rs1,rs2" in machine code is "1000000[rs2][rs1]111[rd]0000000"

#sample code = 
"""
0000000 rs2 rs1 000 rd 0110011 : add rd, rs1, rs2
0000000 rs2 rs1 110 rd 0110011 : or rd, rs1, rs2
imm[11 : 0] rs1 010 rd 0000011 : lw rd, imm[11:0](rs1)
imm[12|10 : 5] rs2 rs1 000 imm[4 : 1|11] 1100011 :  beq rs1, rs2, imm[12:1]
a1 = 01011
a2 = 01100
a7 = 10001
53 = 110101

converts to: 
add a7, a1, a2
or a7, a1, a2
lw a7, 53(a2)

0000000 01100 01011 000 10001 0110011
0000000 01100 01011 110 10001 0110011
 000000110101 01100 010 10001 0000011
0000000 00000 00000 000 00000 1100011
 
This is the sample I will write the requirments in
"""

#AKSHAT
# program stub to make a dictionary with name = "code"
# returns a dictionary of the form {line number(in bytes)<int> : [line<str> , instruction type<char/str>]}
# write "bonus" for the bonus instructions
# for the example, it will finish with a dictionary code = {0 : ["00000000110001011000100010110011" , "R"],
#                                                           4 : ["00000000110001011110100010110011" , "R"],
#                                                           8 : ["00000011010101100010100010000011" , "I"],
#                                                          12 : ["00000000000000000000000001100011" , "B"]]}


#JASJYOT
# program stub to convert binary to decimal which takes 2 arguments, number of bits<int> 
# and the number <str> and returns a decimal number<int>

global registers
registers = { "00000" : ["zero" , 0] ,
              "00001" : ["ra" , 0]  ,
              "00010" : ["sp" , 0]  ,
              "00011" : ["gp" , 0]  , 
              "00100" : ["tp" , 0]  ,
              "00101" : ["t0" , 0]  ,
              "00110" : ["t1" , 0]  ,
              "00111" : ["t2" , 0]  ,
              "01000" : ["s0" , 0]  ,  
              "01001" : ["s1" , 0]  ,
              "01010" : ["a0" , 0]  , 
              "01011" : ["a1" , 0]  , 
              "01100" : ["a2" , 0]  , 
              "01101" : ["a3" , 0]  , 
              "01110" : ["a4" , 0]  ,
              "01111" : ["a5" , 0]  , 
              "10000" : ["a6" , 0]  , 
              "10001" : ["a7" , 0]  , 
              "10010" : ["s2" , 0]  , 
              "10011" : ["s3" , 0]  , 
              "10100" : ["s4" , 0]  , 
              "10101" : ["s5" , 0]  , 
              "10110" : ["s6" , 0]  , 
              "10111" : ["s7" , 0]  , 
              "11000" : ["s8" , 0]  , 
              "11001" : ["s9" , 0]  , 
              "11010" : ["s10" , 0]  , 
              "11011" : ["s11" , 0]  , 
              "11100" : ["t3" , 0]  , 
              "11101" : ["t4" , 0]  , 
              "11110" : ["t5" , 0]  , 
              "11111" : ["t6" , 0]   }
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
          "0x0001007c" : 0,}
 

global program_counter = 4
global stop = 0

def bonus_type(line_to_execute):
    if (line_to_execute == "00000000000000000000000000000000"):
        stop = 1
        return
    if (line_to_execute == "10000000000000000000000000000000"):
        for i in registers:
            registers[i][1] = 0
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
    if type_of_intruction == "U":#JASJYOT
        pass # <=====================================================================================
    if type_of_intruction == "J":#JASJYOT
        pass # <=====================================================================================
    if type_of_intruction == "bonus":
        bonus_type(line_to_execute)

### ALL CODES ABOVE ARE ON SWITCH-CASE BASIS. THEY NEED TO EDIT THE PROGRAM COUNTER AND REGISTERS INTERNALLY.
### If virtual halt ("B" type) or halt ("bonus" type) are found, we need to change the global variable stop and exit loop
