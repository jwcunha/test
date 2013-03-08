"""
Print out the new well number of a 24 well plate's wells after 
pooling into a 96 well plate, or the index of a 384 well plate based on a 96 well's 
location.
"""
#import sys

alpha = 'ABCDEFGHIJKLMNOP'		## Rows of a 96 well plate

alpha384 = {
'A' : ['A','B'],
'B' : ['C','D'],
'C' : ['E','F'],
'D' : ['G','H'],
'E' : ['I','J'],
'F' : ['K','L'],
'G' : ['M','N'],
'H' : ['O','P'] }

sequence = [1,3,5,
            2,4,6,
            7,9,11,
            8,10,12]

def x24_to_96(num_iterations):
	row_number = 0					## row_number(A) = 0
	while row_number <= (num_iterations - 1):
		for col_number in sequence:
			print alpha[row_number] + str(col_number)
		row_number += 1

def x96_to_384_cols_hash(well):
	col = int(well[1:])
	
	col384_2 = col*2
	col384_1 = col384_2 - 1
	
	cols384 = [col384_1, col384_2]
	return cols384
	
def x96_to_384_rows_hash(well):
	row = well[0]
	rows384 = alpha384[row]
	return rows384

def combine(l1,l2):
	one = l1[0] + str(l2[0])
	two = l1[0]	+ str(l2[1])
	three = l1[1] + str(l2[0])
	four = l1[1] + str(l2[1])
	return [one,two,three,four]

def compute_384_index(well):
	'''
	Input: 384 well (e.g. 'B23')
	Output: 384 index (e.g. 47)
	'''
	row_letter = alpha.find(well[0])
	base = row_letter * 24
	add_col = int(well[1:])
	
	index = base + add_col
	return index

def x96_to_384(plate_numb, well):
	'''
	Input: A 96 well plate, e.g. 3, and a well on the plate, e.g. B5
	Output: Index of the well on a 384 well plate, e.g. 10, and the well, e.g. A10
	'''
	cols_list = x96_to_384_cols_hash(well)           #e.g. A8 --> X15,16
	rows_list = x96_to_384_rows_hash(well)           #e.g. A8 --> A,B
	wells384 = combine(rows_list,cols_list)          #e.g. A8 --> ['A15', 'A16', 'B15', 'B16']
	
	well_trnsl = wells384[plate_numb-1]            #e.g. (3,'A8') --> 'B15'
	well_index = compute_384_index(well_trnsl)     #e.g. (3,'A8') --> 39
	
	return well_trnsl, well_index                #e.g. ('B15', 39)


	
