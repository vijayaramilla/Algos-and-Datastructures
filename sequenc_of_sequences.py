"""
parse the input. fun1
create the given number of empty sequences
iterate over the number of iter present in the input
for each query:
    1. Find the seq list using the given formula func2
    2. If the first value is 1, append the integer to the seq list found above
    3. Else calucate the value and update he lastAnswer and print.func2
"""

def executeQuery1(x, y):
    seq_id = (x ^ lastAnswer) % N
    master_list[seq_id].append(y)
    
def executeQuery2(x, y):
    global lastAnswer
    seq_id = (x ^ lastAnswer) % N
    index = y % len(master_list[seq_id])
    lastAnswer = master_list[seq_id][index]
    return lastAnswer
 

def parse_input() :
    input_list = (input().split(" "))
    global N
    N = int(input_list[0])
    Q = int(input_list[1])
    global lastAnswer
    lastAnswer = 0
 
    #Create list of N empty lists
    global master_list
    master_list = []
    for i in range(0, N):
        sub_list = []
        master_list.append(sub_list)

   
    #iterate the number of queries
    for i in range(Q):
        #read the query and call the appropriate function
        args = list(map(int, input().split(" ")))
        if args[0] == 1:
            executeQuery1(args[1], args[2])
        else:
           
            sol = executeQuery2(args[1], args[2])
            print (sol)
parse_input()
