def func():
    print("me")

def func_caller(func):
    func()

func_caller(func)