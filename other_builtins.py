# -------------- zip() verbindet Listen im Reißverschlussprinzip -------------------

games = ["Schach", "Tennis", "Fussball"]
player= ["Karpov", "Becker", "Messi"]
origin = ["Russland", "Deutschland", "Argentinien"]

both =zip(player,games)
all3 = zip(player, games, origin)
bothAsDict = dict(zip(player,games))

for pair in both:
    print (pair)

for triple in all3:
    print (triple)

print (bothAsDict)

# -------------- Ende zip() -------------------------------------------------------

# -------------- filter() entfernt Listeneinträge mit bestimmtem Merkmal ----------

def myFunc(x):
  if x == "Schach":
    return False
  else:
    return True
  
aShortFunc = lambda x: x!= "Schach" # myFunc als Lambda- Funktion

filtered = filter(aShortFunc, games)

for x in filtered:
  print(x)

# -------------- Ende filter() ----------------------------------------------------

# -------- enumerate() ergänzt eine Liste/ Tupel etc mit dem jeweiligen Index -----

print(list(enumerate(games)))
print(list(enumerate(zip(player, games, origin))))
print(list(enumerate(all3)))
print(list(enumerate(bothAsDict)))
print(list(enumerate(bothAsDict.items())))

for index, (key, value) in enumerate(bothAsDict.items()):
    print(index, key, value)


# -------------- Ende enumerate() -------------------------------------------------

# -------------- List Comprehension -----------------------------------------------

zahlen =[1,2,3,4,5,6,7,8,9,10]
filter_zahlen = [zahl for zahl in zahlen if (zahl%2 == 0)]

# zahl*2 for zahl in zahlen if ((zahl*3)<15)
# zahl*4 for zahl in zahlen if ((zahl*3)%8==0)
print(zahlen)
print(filter_zahlen)

namen =["Udo", "Susanne", "Beate", "Tom", "Chris"]
filter_namen = [name for name in namen if (len(name)<4)]
# len(name)<4
# len(name)>3 & len(name)<7
# name.endswith("e")
print(filter_namen)
# -------------- Ende List Comprehension ------------------------------------------