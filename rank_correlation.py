

def str_to_lis(string): 
    result = []
    without_whitespace = string.strip()
    raw_x = without_whitespace.split(sep = ",")
    for value in raw_x:
        result.append(int(value))
    return result

# x  = str_to_lis("8,10,12,6,9,14,18,16")
# y = str_to_lis("15,25,18,20,16,21,10,12")

# str_to_lis(x,'X')
# str_to_lis(y,'Y')

# while len(x) != len(y):
#     if len(x) > len(y):
#         x.pop(-1)
#     if len(y) > len(x):
#         y.pop(-1)


# # print(f"{x} >> {rank_x}")
# # print(f"{y} >> {rank_y}")

# d = []
# zip_object = zip(rank_x, rank_y)
# for list1_i, list2_i in zip_object:
#     d.append(list1_i-list2_i)
# print(d)

# d_squared = [number ** 2 for number in d]
# print(d_squared)


def calc_rank_correlation(X,Y):
    while len(X) != len(Y):
        if len(X) > len(Y):
            X.pop(-1)
        if len(Y) > len(X):
            Y.pop(-1)
    def rank(arr):
        rankorderofsomelist = [len(arr)-(sorted(arr).index(n)) for n in arr]
        return rankorderofsomelist
    rank_x = rank(X)
    rank_y = rank(Y)
    d = []
    zip_object = zip(rank_x, rank_y)
    for list1_i, list2_i in zip_object:
        d.append(list1_i-list2_i)
    d_squared = [number ** 2 for number in d]
    # Calculating the sum of d_squared
    sumo = 0
    for i in d_squared:
        sumo = sumo+i
    length = len(X)

    #Final formula
    val = 6 * sumo
    den = (length *  (length ** 2)- 1)
    r= 1 - val / den
    return round(r,2)

