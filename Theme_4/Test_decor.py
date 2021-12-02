# декоратор

def simple_decor(fn):
    def wrapper():
        print('Сейчас запустится функция')
        fn()
        print('Функция отработала')
    return wrapper

@simple_decor
def some_func():
    print('Функция работает')

some_func()