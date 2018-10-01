"""
JSON Comparator

Write a program that takes two strings in JSON format and compares them. The program should output the difference between those JSON strings.

For example:
Input:
{"a": 2, "b": 3}
{"a": 2, "b": 4}
Output: 
"b": 3
"b": 4

Input:
{"a": "hello", "b": {"c": 3}}
{"a": "hello", "b": {"c": 11}}
Output:
"b": {"c": 3}
"b": {"c": 11}
"""
import json
x='{"a": "hello", "b": {"c": 3},"d":4}'
y='{"a": "hello", "b": {"c": 11},"d":8}'
a=json.loads(x) #Convert json data to python dict
b=json.loads(y)
#print (a) #==>{'a': 'hello', 'b': {'c': 3}}
#NOTE: We assume that lenght of jsons are equal
for key, value in a.items():
    if (a[key]!=b[key]):
        print ("Differences at {} key which are :  {}, {}".format(key,a[key],b[key]))













