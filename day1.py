#day 1 part 1
#find the fuel required for a module, take its mass, divide by three, round down, and subtract 2

#part1 function
def fuel_required(mass):
    if(mass < 0):
        return 0
    else:
        return (mass/3 - 2)

#part2 fucntion
def total_fuel(mass):    
    total = 0
    while(fuel_required(mass) >= 0):
        total += fuel_required(mass)
        mass = fuel_required(mass)
    return total

input_file = open('input.txt','r')
total_fuel_1 = 0
total_fuel_requirement = 0
list_of_masses = input_file.readlines()

for i in list_of_masses:
    total_fuel_1 += fuel_required(int(i))
print("part1 = " + str(total_fuel_1))

for i in list_of_masses:
    total_fuel_requirement += total_fuel(int(i))

print("part2 = " + str(total_fuel_requirement))
