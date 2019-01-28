def benchmark(func):
    ''' standard benchmarking decorator'''

    from time import clock

    def wrapper(*args, **kwargs):
        t=clock()
        res=func(*args, **kwargs)
        print('functions: ', func.__name__, 'benchmark: ', clock()-t, 's')
        return res
    return wrapper
