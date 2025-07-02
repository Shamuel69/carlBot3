import math

### indi = individual 

def adjustable_matrix(height: int, rows:int):
    mother_exponent = -11.62413
    slope = 202.14817
    MF_value = slope*(height**mother_exponent)
    matrix = []
    
    for iter in range(height):
        mini_matrix = []
        for i in range(rows):
            indi_value = rows-((slope*(height**mother_exponent))**i)
            print((slope*(height**mother_exponent))**i)
            mini_matrix.append(indi_value)
        matrix.append(mini_matrix)   
    
    return matrix

def bingus(longways:int):
    var = []
    
    max_range = 255
    mother_exponent = -11.62413
    slope = 202.14817


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

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(x) for x in row))

# bingus(100)
print(adjustable_matrix(20, 5))