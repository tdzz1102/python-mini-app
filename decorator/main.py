from time import sleep
from datetime import datetime

def deco(tag):
    def _deco(func):
        def w():
            start = datetime.now()
            func()
            end = datetime.now()
            print(tag)
            print(end - start)
            return 0
        return w
    return _deco

# decoに引数を渡すため、ネスト・デコレータが必要
@deco('/')
def f():
    sleep(1)

# まるでw()を呼び出しているような
a = f()
print(a)