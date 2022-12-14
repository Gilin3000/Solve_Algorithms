import sys
# import heapq
# from collections import deque
input = sys.stdin.readline

N = int(input())
N_arr = [[] for _ in range(N+1)]
N_arr[0] = 0
N_arr[1] = 1

result = 0

def fibonachi(num):
    global result

    if N_arr[num] != []:
        return N_arr[num]
    else:
        N_arr[num] = fibonachi(num-1) + fibonachi(num-2)
        result += 1
        return N_arr[num]
    

print(fibonachi(N))
print(result-1)