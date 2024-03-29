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

# program stub to make a dictionary
# returns a dictionary of the form {line number(in bytes)<int> : [line<str> , instruction type<char/str>]}
# write "bonus" for the bonus instructions
# for the example, it will finish with a dictionary code = {0 : ["00000000110001011000100010110011" , "R"],
#                                                           4 : ["00000000110001011110100010110011" , "R"],
#                                                           8 : ["00000011010101100010100010000011" , "I"],
#                                                          12 : ["00000000000000000000000001100011" , "B"]]}


# program stub to iterate through the entire code and find errors, raise errors if any
# possible errors till now - undefined opcode
#                            virtual halt not present/not at the end
#                            ...(maybe more to be added)


# program stub to convert binary to decimal which takes 2 arguments, number of bits<int> 
# and the number <str> and returns a decimal number<int>


#registers = {0:value of 0<int> , 1:value of 1<int> ... 31:value of 31<int>}


# global variable program_counter = 0
# global variable stop = 0



# while loop => while stop == 0:
# line_to_execute = dictionary[program_counter][0]
# type_of_intruction = dictionary[program_counter][1]

# code to execute R type instruction
# code to execute I type instruction
# code to execute S type instruction
# code to execute B type instruction (needs to break loop if "00000000000000000000000001100011" found)
# code to execute U type instruction
# code to execute J type instruction
# code to execute bonus type instruction

### ALL CODES ABOVE ARE ON SWITCH-CASE BASIS. THEY NEED TO EDIT THE PROGRAM COUNTER AND REGISTERS INTERNALLY.
### If virtual halt ("B" type) or halt ("bonus" type) are found, we need to change the global variable stop and exit loop
