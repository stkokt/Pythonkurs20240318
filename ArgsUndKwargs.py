def sum(a, b):
    return a+b
""" 
def sum(a, b, c):
    return a+b+c """

print(sum(3,4))

def sum(*args):
    print(type(args))
    print(args)
    result=0
    for arg in args:
        result+=arg
    print(result)

sum(1,2,3)

def kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)

kwargs(A=100, B=50)

print()

def briefkopf(*args, **kwargs):
    print(args[0], args[1], '\n')
    print(f"{kwargs.get('Str')} {kwargs.get('Nr')}")
    print(f"{kwargs.get('PLZ')} {kwargs.get('Stadt')}")
    if "Option" in kwargs:
        print(f"{kwargs.get('Option')}")

briefkopf("Stefan", "Koschnik", Str="Bahnhofstr.", Nr="9", PLZ="12345", Stadt="Berlin")
briefkopf("Stefan", "Koschnik", Str="Bahnhofstr.", Nr="9", PLZ="12345", Stadt="Berlin", Option="Beim Nachbarn abgeben")

