def get_my_lst():
    return [1,2,3,4,5]

def my_sum(_lst):
    _sum = 0

    for i in _lst:
        _sum = _sum + i
            
    return _sum

my_lst = get_my_lst()
print(my_sum(_lst = my_lst))
