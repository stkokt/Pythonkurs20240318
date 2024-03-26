int_a=10
int_b=int_a
print(int_a, int_b)
int_a=11
print(int_a, int_b)
int_a=1
int_b=3
print(int_a.bit_count()) # Sogar Integervariablen haben Methoden
# 0000 0000
# 0000 0001
# 0000 0010
# 0000 0011
# Little/ Big Endian
# 01.01.2024
# 2024/01/01
# int_c=(bin(int_a) and bin(int_b)) # Konvertieren zu einer Binärrepräsentation der Integerzahl
print(~int_a) # Verwirrend, weil hier der Negativwert der Integerzahl ausgegeben wird
#print(bin(int_b))


# Float

float_a=1043.791454
print(round(float_a, -3)) # Runden bis in den Vorkommabereich

print(int(float_a))

float_b=1.9999999999999999 # 16 9er-Nachkommastellen ->
print(int(float_b)) # Nachkommastellen werden in diesem Fall nicht abgeschnitten, sondern Rundung auf 2

# import math # Bibliotheken/ Module können an jeder Stelle des Codes eingebunden werden
from math import floor
from math import ceil

print(ceil(float_b)) # Unschärfeverhalten bleibt auch mitn den Mathemodulen

# Listen

list_a=[1,2,3,4,5,6,7,8,9,10]
print("ID vor Reverse")
print(list_a)
print(id(list_a))
print(id(list_a[0]))    # Lesender Zugriff auf das erste Element der Liste
list_a[3]=10    # Schreibender Zugriff auf das erste Element der Liste
print(list_a[0:5:2]) # List-Sclicing -> Vom ersten Index bis VOR den 5. Index in 2er Schritten
print(len(list_a)/2) # Berechnen der Hälfte der Liste
print(list_a[0:int((len(list_a)/2))]) # Benutzung eines generischen Indexes
list_a.reverse()    # Reversemethode kann nicht als Zuweisung genutzt werden
print("ID nach Reverse")
print(list_a)
print(id(list_a))   # Wo im Arbeitsspeicher liegt die Liste?
list_b=list_a[::-1] # Shorthand für eine Reverse-List, kann in Zuweisung genutzt werden
print(list_b)
print(list_a[3:5:2])

list_c=[x for x in range(0,21, 2)]  # List- Comprehension für generische Liste
print(list_c)
print(list_b[::-4])

list_d=list_b
print(list_b, list_d)
list_b[0]=100
print(list_d)

list_f=["a", "b", "c"]
list_g=["d", "e", "f"]

print(list_f+list_g)

#list_f.append(list_g)  # Hängt Liste G als Liste an Liste F
print(list_f)
list_f.extend(list_g)   # Erweitert die Liste F um die Elemente der Liste G
print(list_f)

# Listen Methoden: append, extend, copy, count, index, insert, pop, remove, reverse, sort

list_h=[1,2,4,1,5,1,2,3]
print(list_h.count(2))
print(list_h.index(2,3))
list_h.sort(reverse=0)
print(list_h)

list_i=[1,5,4]
list_j=[2,3,4]

list_k=list_i+list_j    # Wie List.extend()
var=set(list_k)         # Konvertierung in Set entfernt Duplikiate, ändert aber die Reihenfolge
print(all(list_i), any(list_i)) # Builtin Funktionen, die prüfen, ob ein oder alle Elemente der Liste True sind

#



