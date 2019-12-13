#intcode list of integers
#99 program is finished and should be halt
#1 adds number from two positions and stores in 3rd position
#the number after 1 defines the position not the number to be added
#2 multiplies the same as above
#skip 4 positions ahead after the opcode is done

#def opone(first_pos, second_pos, third_pos):
 #   input_array 

input_values = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,23,9,27,1,5,27,31,2,31,13,35,1,35,5,39,1,39,5,43,2,13,43,47,2,47,10,51,1,51,6,55,2,55,9,59,1,59,5,63,1,63,13,67,2,67,6,71,1,71,5,75,1,75,5,79,1,79,9,83,1,10,83,87,1,87,10,91,1,91,9,95,1,10,95,99,1,10,99,103,2,103,10,107,1,107,9,111,2,6,111,115,1,5,115,119,2,119,13,123,1,6,123,127,2,9,127,131,1,131,5,135,1,135,13,139,1,139,10,143,1,2,143,147,1,147,10,0,99,2,0,14,0]

input_keys = [i for i,e in enumerate(input_values)]

#make a dictionary with the position of the element as key and the value as the element iself
input_dict = {}

for i in input_keys:
    input_dict[i] = input_values[i]

print(len(input_values))
x = 0
k = input_keys[x]

while( k < len(input_values)):
    v = input_dict[k]
    #print(k , v)
    if(v == 1):
        input_dict[input_dict[k+3]] = input_dict[input_dict[k+1]] + input_dict[input_dict[k+2]]
    elif(v == 2):
        input_dict[input_dict[k+3]] = input_dict[input_dict[k+1]] * input_dict[input_dict[k+2]]
    elif(v == 99):
        break
    k = k + 4

for k,v in input_dict.iteritems():
    print(k, v)
