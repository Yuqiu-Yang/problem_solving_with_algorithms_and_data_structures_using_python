import timeit

for i in range(100000, 1000001, 100000):
    t = timeit.Timer("x[500]", "from __main__ import x")
    x = list(range(i))
    fst_time = t.timeit(number = 10000)
    print("Time for indexing a list of length %d is %f "% (i,fst_time))
for i in range(100, 1001, 100):
    t = timeit.Timer("x = {j:None for j in range(%d)}"%i, "from __main__ import x")
    x = {}
    sst_time = t.timeit(number = 10000)
    print("Time for generating a dictonary of size %d is %f" % (i, sst_time))
