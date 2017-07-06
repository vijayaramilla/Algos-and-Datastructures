# find the sqare integers between 2 given numbers inclusive
import math

# find the square root of a and b and take the differnce
def get_squares(a, b):
    count = 0
    square1 = math.ceil(math.sqrt(a))
    square2 = math.floor(math.sqrt(b))
    count = square2 - square1 + 1 
    return count

def parse_input():
    N = int(input())
    for i in range(N):
        A, B = map(int, input().split(" "))
        res = get_squares(A, B)
        print(res)

parse_input()


