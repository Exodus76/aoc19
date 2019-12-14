#intcode list of integers
#99 program is finished and should be halt
#1 adds number from two positions and stores in 3rd position
#the number after 1 defines the position not the number to be added
#2 multiplies the same as above
#skip 4 positions ahead after the opcode is done

#def opone(first_pos, second_pos, third_pos):
 #   input_array 
import itertools

arr = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,23,9,27,1,5,27,31,2,31,13,35,1,35,5,39,1,39,5,43,2,13,43,47,2,47,10,51,1,51,6,55,2,55,9,59,1,59,5,63,1,63,13,67,2,67,6,71,1,71,5,75,1,75,5,79,1,79,9,83,1,10,83,87,1,87,10,91,1,91,9,95,1,10,95,99,1,10,99,103,2,103,10,107,1,107,9,111,2,6,111,115,1,5,115,119,2,119,13,123,1,6,123,127,2,9,127,131,1,131,5,135,1,135,13,139,1,139,10,143,1,2,143,147,1,147,10,0,99,2,0,14,0]

temp = arr.copy()

#part-2
for x in range(0,100):
  for y in range(100,-1,-1):
    arr = temp.copy()
    arr[1] = x
    arr[2] = y
    count = 0
    #part 1
    while(True):
        z = arr[count]
        if(z == 1):
            arr[arr[count+3]] = arr[arr[count+1]] + arr[arr[count+2]]
        elif(z == 2):
            arr[arr[count+3]] = arr[arr[count+1]] * arr[arr[count+2]]
        elif(z == 99):
            break;
        count = count + 4
    if(arr[0] == 19690720):
        print(arr[0],arr[1],arr[2])
        print("answer = ", 100 * arr[1] + arr[2])
        break
