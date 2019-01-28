def benchmark(func):
    ''' standard benchmarking decorator'''

    from time import clock

    def wrapper(*args, **kwargs):
        t=clock()
        res=func(*args, **kwargs)
        print('method: ', func.__name__, 'timing: ', clock()-t, 's')
        return res
    return wrapper
