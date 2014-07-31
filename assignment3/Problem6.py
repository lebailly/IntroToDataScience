import sys, MapReduce

"""
This program will multiply two matrices. The input to the map function will be 
a row of a matrix represented as a list. Each list will be of the form 
[matrix, i, j, value] where matrix is a string and i, j, and value are integers.

The first item, matrix, is a string that identifies which matrix the record 
originates from. This field has two possible values: "a" indicates that the 
record is from matrix A and "b" indicates that the record is from matrix B
"""

mr = MapReduce.MapReduce()

# Matrix 'a' has dimensions of LxM
# Matrix 'b' has dimensions of MxN

L = 5
M = 5
N = 5

def mapper(record):
    #The key is the location in product matrix.
    #The value is a tuple.  The first element is the position used when 
    #multiplying elements in the reducer, the second is the matrix value.

    value = record[3] # Value in matrix

    if(record[0] == 'a'): # Element is in first matrix, labeled 'a'
        row = record[1]
        for k in range(N):
            mr.emit_intermediate((row,k),(record[2],value))
    else:
        col = record[2]
        for i in range(L):
            mr.emit_intermediate((i,col),(record[1],value))

def reducer(key, list_of_values):
    # key: The location in the product matrix.
    # value: list of positions and values.

    elements = [1]*M
    counts = [0]*M

    for position, value in list_of_values:
        elements[position] *= value
        counts[position] += 1

    for position, value in enumerate(elements):
        if(counts[position] != 2): elements[position] = 0

    mr.emit((key[0], key[1], sum(elements)))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)