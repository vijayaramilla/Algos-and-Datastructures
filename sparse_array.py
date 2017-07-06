"""
string and occurance of given string.
use dictionary to save the strings and their counts.
1. parse_input():
    a. read N.
    b. read the N strings and populate the dictionary.
    c. read q
    d. for each query in q:
        a. call the get count method
        b. print he count
2. get_count(string):
    a. for the given string, check if the string is present in the dict
    b. if present:
        a. return the count
       else: 
        a. return 0      
""" 
global sparse_list
sparse_list = {}

def get_count(string):
    if string in sparse_list:
        return sparse_list[string]
    else:
        return 0

def parse_input():
    N = int(input())
    for i in range(N):
        string = input()
        if (string  in sparse_list):
            sparse_list[string] += 1
        else:
            sparse_list[string] = 1
            
    #proces the queries:
    q = int(input())
    for i in range(q):
        query = input()
        res = get_count(query)
        print(res)
    
parse_input()
