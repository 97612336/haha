# print('qwe%s'%'你好')
# print('haha,{}{}'.format('123','有一个'))
# # print('asd%s'%(1,2,3))
# print('asd{}'.format((1,2,3,4,5)))


# print(enumerate((1,23,45,6)))
import celery


def show(fn):
    def wrapper():
        return fn()+123
    return wrapper

@show
def go():
    print('nihao')
    return 123

# print(go())


app=celery.Celery('t03',broker='redis://127.0.0.1')

@app.task 
def go_test():
    for i in range(10):
        print(i)

go_test()