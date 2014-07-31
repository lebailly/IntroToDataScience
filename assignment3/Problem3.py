import sys, MapReduce

"""
Consider a simple social network dataset consisting of a set of key-value pairs 
(person, friend) representing a friend relationship between two people. 
This program uses a MapReduce algorithm to count the number of friends 
for each person.
"""

mr = MapReduce.MapReduce()

def mapper(record):
    #The key is the person name
    key = record[0]

    #Record[1] = friend's name, but we don't need that here.
    mr.emit_intermediate(key, 1)

def reducer(key, list_of_counts):
    # key: person name
    # value: list of friend counts

    mr.emit((key,sum(list_of_counts)))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)