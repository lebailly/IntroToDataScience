import sys, MapReduce

"""
A relational join done in Map-Reduce which executes the following SQL command:

SELECT * 
FROM Orders, LineItem 
WHERE Order.order_id = LineItem.order_id

The input is one big concatenated bag of records.  The first element is table
name, the second it the order_id, followed by the remainig fields of the table.
"""

mr = MapReduce.MapReduce()

def mapper(record):
    #The key is the join index (order_id, in this case)
    key = record[1]

    #The entire record is the value.
    
    mr.emit_intermediate(key, record)

def reducer(key, list_of_records):
    # key: order_id
    # value: list of records

    for order_item in list_of_records:
      if(order_item[0] == 'order'):
        for line_item in list_of_records:
          if(line_item[0] != 'order'):
            mr.emit(order_item+line_item)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)