def sum(x,y):
    assert(type(x) == int and type(y) == int), 'one val is not an int'
    k = x+y
    assert(k < 100),'sum is over 100'
    return k

print sum(23,5)


