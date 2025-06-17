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
    for i in range(n):
        mini_list.append(i)
        if i % Width:
            matrix.append(mini_list)
            
            print("fuck yeah")


bingus(100)