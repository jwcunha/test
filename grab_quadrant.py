"""
Get the quadrant you want from a .csv of 384 well reader plate data.
"""

### Maybe it would make sense to make this a method on the cell object - get your quadrant?

from well_conversion import *

## The x96_to_384 function returns a tuple of the well and well index (e.g. 'B5',283).
## I am going to build a for loop that will get the well index for every well in a given
## quadrant.

wells_96 =  ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 
			 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 
			 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 
			 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 
			 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12', 
			 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 
			 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 
			 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12']

def get_that_well(quadrant, well_list=wells_96):
	"""
	Input:	The desired quadrant (e.g. 1) and a list of the wells in a 96 well plate.
	Output:	A list of the well 384 well indices of each well in the quadrant.
	"""
	new_list = []
	for well in well_list:
		index_384 = x96_to_384(quadrant,well)[1]     #grab 384 index for each well on 96 WP
		new_list.append(index_384)
	return new_list


 
index_384_list = get_that_well(1)		# first quadrant

file = open('output_deep_well.csv','r')
output_file = open('just_quadrant_one_deep_well.csv','w')


file.readline()
file.readline()
file.readline()
file.readline()
file.readline()
file.readline()
file.readline()
file.readline()
file.readline()

counter = 1
well_counter = 0

header = ['96 Well', ' 0', ' 45', ' 90', ' 135', ' 180', ' 225', ' 270', ' 315', 
		  ' 360', ' 405', ' 450', ' 495', ' 540', ' 585']
		  
for i in header:
	output_file.write(i+', ')
output_file.write('\n')


while counter < 394:
	if counter in index_384_list:
		data_grab = file.readline()
		data_96_well = wells_96[well_counter]
		output_file.write(data_96_well + ', ' + data_grab)
		well_counter += 1
	else:
		file.readline()
	counter += 1


file.close()
output_file.close()


