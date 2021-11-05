my_lst = [1,2,3,4,5]


def sum_list(my_lst):
    for i in range (len(my_lst)):
        x = my_lst[i] + (my_lst[i] + 1) #???
        
    return x

sum_list(my_lst)

print(sum_list(my_lst))
