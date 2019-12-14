input_file = open('input_day3.txt','r')

input_data = input_file.readlines()

first_wire = input_data[0].rstrip().split(',')
second_wire = input_data[1].rstrip().split(',')

# first_wire[-1].rstrip()

#keep track of their positions
# position_one

# position_two

#lets take cartesian plane wwith x,y = 0,0 initially
#we will get the ranges of the positions

def get_points(wire):
	points = []
	x = 0
	y = 0
	for i in wire:
		if 'U' in i:
			i = int(i.strip('U'))
			y = y + i
			points.append(tuple((x,y)))
			continue
		if 'D' in i:
			i = int(i.strip('D'))
			y = y - i
			points.append(tuple((x,y)))
			continue
		if 'L' in i:
			i = int(i.strip('L'))
			x = x - i
			points.append(tuple((x,y)))
			continue
		if 'R' in i:
			i = int(i.strip('R'))
			x = x + i
			points.append(tuple((x,y)))
			continue
	return points

first_wire_ranges = get_points(first_wire)

print(len(first_wire_ranges))

second_wire_ranges = get_points(second_wire)
print(len(second_wire_ranges))

for i in first_wire_ranges:

	for j in second_wire_ranges:
		(x1 - x2)()-()()