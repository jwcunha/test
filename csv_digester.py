"""
Since .csv/.xls data comes out of the robot as one very long row, we need to 
break it up into its component rows of 14 columns. The following script splits the
row into one long list and then outputs a usable .csv file.
"""

import sys

def parsed_to_list(parsed_input_file):
	"""
	Input: 	A parsed .csv or .xls spreadsheet, split along the comma using the .split(',')
			method. It is a list of values that contains extraneous characters.
	Output: A clean list of values for each well in the plate.
	"""
	new_list = []
		
	for cell in parsed_input_file:
		cell = cell.split('\r')			# if annoying line break character is there, 
		if len(cell) > 1:				# get rid of it
			new_list.append(cell[0])
			new_list.append(cell[1])
		else:
			new_list.append(cell[0])
		
	return new_list	
	

def fourteen_blocks(clean_list, output_file):
	"""
	Input: 	Clean list from parsed_to_list(), open empty output file.
	Output:	A .csv file that makes sense (i.e. isn't one long row, contains
			multiple rows of 14 columns).
	"""
	cell_index = 1            # for keeping track of what column we are in
	
	for cell in clean_list:
		if cell_index == 14:
			output_file.write(cell+'\n')	# end of row
			cell_index = 1
		else:					# we are not yet at the end of a row			
			output_file.write(cell+', ')	# comma is necessary for rendering cells in .csv
			cell_index += 1
		
## The script:
input_file = sys.argv[1]
output_file = sys.argv[2]

f = open(input_file,'r')						# open the input .csv file

parsed_input_file = f.readline().split(',')		# split that big row into a list
f.close()

new_output_file = open(output_file,'w') 		# name your output .csv file

clean_list = parsed_to_list(parsed_input_file)		# clean up parsed input file

fourteen_blocks(clean_list, new_output_file)		# turn cleaned up list into a .csv

new_output_file.close()