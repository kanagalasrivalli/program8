def smallest_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print(smallest_num_in_list([5,3,2,1,7,6,10,8,9]))
