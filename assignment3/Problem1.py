import sys, MapReduce

"""
Create an Inverted index. Given a set of documents, an inverted index is a 
dictionary where each word is associated with a list of the document 
identifiers in which that word appears.
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: a single word (w)
    # value: document identifier (doc_id)

    doc_id = record[0]
    words = record[1].split()

    for w in words:
      mr.emit_intermediate(w, doc_id)

def reducer(key, list_of_values):
    # key: word
    # value: list of document identifiers

    total = list(set(list_of_values)) #Removes duplicates
    
    mr.emit((key, total))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)