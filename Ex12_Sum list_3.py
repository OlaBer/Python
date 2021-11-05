my_lst = ["1","2","3","4","5","6"]


def fun(_lst):

    _sum = ""

    for element in _lst:
        _sum = _sum + element

    return _sum 

print(fun(my_lst))
