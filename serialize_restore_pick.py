import pickle


class Foo:
    attr = 'A class attribute'

    def __init__(self, x):
        self.x = x
        if x > 0:
            self.child = Foo(x-1)

    def hello(self):
        print("Hello World")


f = Foo(3)
p = pickle.dumps(f)
print(p)
