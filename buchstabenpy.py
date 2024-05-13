buchstaben = ['H','a','l','l','o','l','l']
print(buchstaben)

def entferne(liste,raus):
 for step in liste:
    if step == raus:
        liste.remove(step) # remove- Methode des Datentyps Liste (Übergabeparameter: Wert)
        entferne(liste,raus)

""" entferne(buchstaben,'l')

print(buchstaben) """

zahlen=[6,7,7,8,9]

# pop- Methode, die zu dem Datentyp Liste gehört (Übergabeparameter: Index)
zahl=[]

# Die beiden folgenden Zeilen verändern auch die Liste Zahlen
""" zahl.extend([zahlen.pop(3)])
zahl.extend([zahlen.pop(1)]) """

""" text="Hallo"
print(text.find("lo")) """

""" entferne(zahlen,2)"""

print(zahl)

e=(1,2)
f=(2,2)

print(e>f)

s = "Karriere Tutor!"
s = s.lower()
s = s.capitalize()
print(s)
s = s.split(" ")
print(s)
t = [elem[0] for elem in s]
print(t)

isEven=lambda x: x%2==0

z=[elem for elem in zahlen if isEven(elem)]
print(z)
