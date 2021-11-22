

def str_to_lis(string): 
    result = []
    without_whitespace = string.strip()
    raw_x = without_whitespace.split(sep = ",")
    for value in raw_x:
        result.append(int(value))
    return result

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

