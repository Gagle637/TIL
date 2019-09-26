def hello(func):
    def wrapper():
        print('HIHI')
        func()
        print('hahaha')
    return wrapper

@hello
def bye():
    print('byebye')

bye()