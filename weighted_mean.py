def calc_wmean(n, x, w):
    total_wt = 0
    for i in range(n):
        total_wt += x[i] * w[i]
    mean = total_wt / sum(w)
    return mean
    
def parse_input():
    N = int(input())
    X = list(map(int, input().split(" ")))
    W = list(map(int, input().split(" ")))
    
    wm = calc_wmean(N, X, W)
    print ("%.1f" % wm)

parse_input()
