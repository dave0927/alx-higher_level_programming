#!/usr/bin/python3
def multiply_by_2(my_dict):
    tmp_dict = my_dict.copy()
    for i in tmp_dict.keys():
        tmp_dict[i] *= 2
    return (tmp_dict)
