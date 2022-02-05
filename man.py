class Man:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello, " + self.name + "!")

    def goodbye(self):
        print("Goodbye, " + self.name + "!")

m = Man("Neil")
m.hello()
m.goodbye()
