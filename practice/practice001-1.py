# def printinfo1(a,*b):
#     print(a)
#     for i in b:
#         print(i)
#     return
#
# printinfo1(70,50,60)
#
#
# def printinfo2(a,**b):
#     print(a)
#     print(b)
#     for i in b:
#         print(i)
#     return
#
# printinfo2(70,s=1,d=2,c=3)

def decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")

    return wrapper

def func_a():
    print("real func")



func_a=decorator(func_a)

func_a()
print(func_a.__name__)


print("==========")

@decorator
def func_b():
    print("real func_b")

func_b()

print(func_b.__name__)

print("==========")

from functools import wraps

def decorator_b(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("before again")
        func()
        print("after again")
        return func(*args,**kwargs)
    return wrapper

@decorator_b
def func_c():
    print("real func_c")

func_c()
print(func_c.__name__)


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logit
def addition_func(x):
    """Do some math."""
    return x + x


print(addition_func(4))


def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)

        return wrapped_function

    return logging_decorator


@logit()
def myfunc1():
    pass


myfunc1()


# Output: myfunc1 was called
# 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串

@logit(logfile='func2.log')
def myfunc2():
    pass


myfunc2()
# Output: myfunc2 was called
# 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串