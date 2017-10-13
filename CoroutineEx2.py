def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)

def add(x,y):
    return x+y

def make_handler():
    sequence = 0
    while True:
        print('now sequence:',sequence)
        result = yield #result是send传回的参数
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

if __name__ == "__main__":
    handler = make_handler()
    print('excute make_handle done')
    next(handler)  #执行到yield这句然后中断
    print('excute next done')
    apply_async(add, (2,3), callback=handler.send) #执行了handler.send(add(2,3))也就是回到生成器，并且send值给yield
    print('excute send done')
    apply_async(add, ('hello','world'), callback=handler.send)
    print('excute send done')
