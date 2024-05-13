'''
Immutable Built-in Data Types in Python

Numbers
Booleans
Strings
Bytes
Tuples
frozenset
bytearray

Mutable Built-in Data Types in Python

Lists
Dictionaries
Sets

'''

# ------------ 1. Zahlen sind immutable ----------------
# weil man sie zwar ändern kann, aber sie dabei einen neuen Speicherbereich
# zugewiesen bekommen. Interessant ist, dass der zugewiesene Speicherbereich
# auch von anderen Variablen mit selben Wert genutzt wird:

"""
a=10

print(id(a))

a=11
print(id(a))

b=10
print(id(b))

c=16-6
print(id(c))
 """
# -------------- Ende 1 ---------------------------------

# ------------- 2. Strings sind immutable ---------------
# Hier ist das Speichermanagement ebenso effizient. Jedes Zeichen
# wird unabhängig von der Häufigkeit des Auftretens nur einmal im
# (vermutlich) Heap abgelegt. Im Stack wird ein Pointer angelegt, 
# der dann auf diesen Speicherbereich zeigt:

""" d="Das ist ein String"
print(id(d))
d="Das ist kein String"
print(id(d)) """
""" e="Das ist ein String"
print(id(e),'\n')

for itr in range(len(e)):
    print(id(e[itr]), '=', e[itr])

e_str = list(set([140723101470888,140723101472512,140723101473520,140723101468872,140723101472960,140723101473520,140723101473576,140723101468872,140723101472736,140723101472960,140723101473240,140723101468872,140723101471728,140723101473576,140723101473464,140723101472960,140723101473240,140723101472848]))
e_str.sort()
print(e_str) """

# --------------- Ende 2 ---------------------------------

# ------------- 3. Sets sind mutable ---------------------
# Sets, auch wenn man nicht mit einem Index- Zugriffsoperator die Stellen
# ändern kann, sind mutable, weil man z.B. weitere Stellen anhängen kann
# und der Speicherbereich dennoch unverändert bleibt:
""" f={1,2,3}
print(id(f))

# f[0]=1   wirft Fehler, weil es keinen Zugriffsoperator auf ein einzelnes Element des Sets gibt

f.add(7)
print(id(f), f)
f.pop()
print(id(f), f)
f={1,2,4}
print(id(f))
g={1,2,3}
print(id(g)) """

# --------------- Ende 3 ---------------------------------

# --------------- 4. Listen sind mutable -----------------
# Listen behalten ebenfalls ihren Speicherbereich, wenn sie verändert werden. 
# Auch hier ist zu beobachten, dass gleiche Werte in den Listen auf einen gemeinsamen 
# Speicherbereich referenzieren
""" aList = [5,6,7,8]
print(id(aList), aList)
print(id(aList[3]))

aList[3] = 9
print(id(aList), aList)
print(id(aList[3]))

aList2 = [5,6,7,8]
print(id(aList2), aList2) """

# --------------- Ende 4 ---------------------------------

def func(a: int) -> int:
    pass