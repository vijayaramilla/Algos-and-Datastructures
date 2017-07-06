def populate_arr(n) :
    lst = list(map(int, input().split(" ")))
    return lst
   
        
def cal_median(lst, n):
    #sort the list
    sorted_list = sorted(lst)
       
    if n % 2 == 0 :
        median = ((sorted_list[int(n/2)] + sorted_list[int(n/2)-1])/2)
    else :
        median = (sorted_list[int((n-1)/2)])
    return median 

def find_mode(input_lst):
    max_count = input_lst.count(input_lst[0])
    mode = input_lst[0]
    for i in range(1, len(input_lst)):
        count = input_lst.count(input_lst[i])
        if (input_lst[i] == mode or count < max_count):
            continue
        elif (count == max_count) :
            mode = min(mode, input_lst[i])
        else :    
            count = input_lst.count(input_lst[i])
            max_count = count
            mode = input_lst[i]
    
    return mode

def parse_input() :
    
    N = int(input())
    
    #iterate the array and populate the arr
    input_lst = populate_arr(N)
    
    #calc mean
    
    mean = (sum(input_lst) / len(input_lst))
    print ("%.1f" % mean)
    
    median = cal_median(input_lst, N)
    print("%.1f" %median)
    
    mode = find_mode(input_lst)
    print(mode)
    
parse_input()

