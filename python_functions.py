# Function1

def sign(x):
    if x > 0:
        return 'Positive'
    elif x < 0:
        return 'Negative'
    else:
        return 'Zero'

for x in [-1, 0, 1]:
    print sign(x)


# Example function taking optional keyword arguments

def hello(name, loud=False):
    if loud:
        print 'Hello, %s' % name.upper()
    else:
        print 'Hello, %s!' % name

hello('Devasena')
hello('Pavan', loud=True)

# Python Classes

class Practice:

    # Constructor
    def __init__(self, name):
        self.name = name    # Create an instance variable

    # Instance Method
    def pract(self, loud=False):
        if loud:
            print 'HELLO, %s!' % self.name.upper()
        else:
            print 'Hello, %s' % self.name

p = Practice('Devasena')
p.pract()
p.pract(loud = True) 
