def gener(m, n=0, o=1):
    """
    here we are defining the generator gener
    :param m: manditary parameter
    :param n: default
    :param o: default
    :return:
    """
    if n < m:
        m, n = n, m
    while m < n:
        yield m
        m += o


obj = gener(10)  # obj is object of gener
for i in range(10):
    print obj.next()
