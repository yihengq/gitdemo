import utils
@utils.benchmark

def say_hi():

    print('hello exvivo')

@utils.benchmark
def say_bye():
    print('bye')


if __name__ == '__main__':
    say_hi()
    say_bye()
