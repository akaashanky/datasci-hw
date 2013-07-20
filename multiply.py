import MapReduce
import sys

def mapper(record):
# key: document identifier
# value: document contents
#for every element (i,j) of matrix A, output ((i,k), j, A[i,j]]) for k in 0 to N-1
    for i in range(0,4):
        for j in range(0,4):
            for k in range (0,4):
                if record[0]=='a' and record[1]==i and record[2]==j and record[3]<>0:
                    key = (i,j)
                    mr.emit_intermediate((i,k), (j, record[3]))

    for j in range(0,4):
        for k in range(0,4):
            for i in range (0,4):
                if record[0]=='b' and record[1]==j and record[2]==k and record[3]<>0:
                    mr.emit_intermediate((i,k),(j, record[3]))

def reducer(key, list_of_values):
# key: word
# value: list of occurrence counts
list_of_values.sort()
total = 0
#print key
#print list_of_values
for num in range(len(list_of_values)-1):
    if list_of_values[num][0]==list_of_values[num+1][0]:
        total = total + list_of_values[num][1]*list_of_values[num+1][1]
mr.emit((key[0], key[1], total))

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)