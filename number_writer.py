#number_writer.py
import json
numbers=[2,3,4,5,6,8,9]
filename='numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)
