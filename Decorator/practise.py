####Practise1
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper

@my_logger
def display_info(name,age):
    print('display_info ran with arguments({},{})'.format(name,age))

display_info('John',26)

####Practise2  How long for excuate funtion display_infos time
import time
def my_timer(orig_func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

@my_timer
def display_infos(name,age):
    time.sleep(1)
    print('display_info ran with arguments({},{})'.format(name,age))

display_infos('John',26)

#####Practise3
from functools import wraps
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper

####Practise2  How long for excuate funtion display_infos time
import time
def my_timer(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

@my_timer
@my_logger
def display_infos(name,age):
    time.sleep(1)
    print('display_info ran with arguments({},{})'.format(name,age))

display_infos('Joy',26)

######Decorators With Arguments(Add another layer)
def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed Before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, 'Executed After', original_function.__name__, '\n')
            return result
        return wrapper_function
    return decorator_function


@prefix_decorator('LOG:')
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)
display_info('Travis', 30)
####Example with Flask
from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello():
    return"Hello World!"
@app.route("/about")
def about():
    return"About page"
if __name__=="__main__":
    app.run()
