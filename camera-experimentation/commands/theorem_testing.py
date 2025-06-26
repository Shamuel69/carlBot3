import math


def bingus(longways:int):
    var = []
    
    max_range = 255

    for i in range(longways):
        try:
            # interval_num = int(longways-(longways/max_range)*i)
            interval_num = (longways/max_range)*i

            # glomp = longways+(i-1)(longways[i+1]-longways[i])
            var.append(interval_num)
        except ZeroDivisionError:
            interval_num = longways

            # glomp = longways+(i-1)(longways[i+1]-longways[i])
            print(interval_num)
            var.append(interval_num)
        print(var)

def playing_with_matrix(n:int, Width:int):
    matrix = []
    mini_list=[]
    for i in range(n+1):
        mini_list.append(i)
        if i % Width == 0:
            matrix.append(mini_list)
            mini_list=[]
            continue
        if i==n:
            mini_list.extend([0]*(Width-n%Width))
            matrix.append(mini_list)
    matrix = matrix[1:]
    return matrix

# bingus(100)
print(playing_with_matrix(360, 6))