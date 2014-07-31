import sys, MapReduce

"""
Consider a set of key-value pairs where each key is sequence id and each value 
is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....

This MapReduce program remove the last 10 characters from each string of 
nucleotides, then remove any duplicates generated.
"""

mr = MapReduce.MapReduce()

def mapper(record):
    #The key is the person name
    key = record[1] #Record[0] = seq_id.  Record[1] = DNA sequence
    key = key[:-10]

    #Value not important.  This could be used to count number of keys, if
    #desired in reducer.
    
    mr.emit_intermediate(key, 1)

def reducer(key, list_of_counts):
    # key: Trimmed DNA
    # value: list of 1 for each occurence of trimmed DNA (not used for this app)

    mr.emit(key)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)