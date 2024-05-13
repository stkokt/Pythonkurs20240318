a=10
print(id(a), a)

def aussen ():
    global a
    print(a)
    a=5
    def mitte2():
        a=12
        print(id(a), a)
        def mitte1():
            nonlocal a
            a=13
            print(id(a), a)
        
    print(id(a), a)
aussen()

print(id(a), a)