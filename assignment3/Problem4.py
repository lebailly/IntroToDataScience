import sys, MapReduce

"""
The relationship "friend" is often symmetric, meaning that if I am your friend, 
you are my friend. Here we use a MapReduce algorithm to check whether this 
property holds by generating a list of all non-symmetric friend relationships.
"""

mr = MapReduce.MapReduce()

def mapper(record):
    #The key is both the person name and the friends name.
    #The value is 1 used to count the number of pairs.

    if(record[0] < record[1]):
    	mr.emit_intermediate((record[0],record[1]),1)
    else:
    	mr.emit_intermediate((record[1],record[0]),1)

def reducer(key, friends_count):
    # key: both the person name and the friends name.
    # friends_count: a list contain 1 each time the pair is observed.

    if(len(friends_count) == 1):
	    mr.emit((key[0], key[1]))
	    mr.emit((key[1], key[0]))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)