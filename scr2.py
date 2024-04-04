def bar():
    print("asdfasdf")
    raise Exception("This is an exception from scr2.py")

def foo():
    bar()

foo()