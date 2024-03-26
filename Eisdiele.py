from time import sleep
import os
#Test 123
 
WaffelBecher=0
KugelMax=5
KugelPreis=0.75
Eissorten=("Erdbeer","Zitrone","Joghurt","Vanille","Schoko")
EisDeko=({"artikel":"Sahne ", "preis":0.50}, {"artikel":"Streusel", "preis":0.20})
 
def berechnung()->float:
# Bestellung (Listenabruf*0.75€)
    bestellungSumme=(len(bestellung)*KugelPreis)
    #print("bestellsumme: ", bestellungSumme)
    return bestellungSumme
 
def verabschieden():
    for Kugel in bestellung:
        print(Eissorten[Kugel-1],end=", ")
    #print()
    print("\n","Gesamtbetrag: ",endpreis,"€")
    print("Vielen Dank für ihre Bestellung!")
    input("Enter für neue Bestellung.")
 
def berechneMWST(brutto:float)->float:
    return(brutto/119*19)
 
 
while True:
    auswahlBecher=False
    auswahlEissorten=False
    bestellung=[]
    bestellungDeko=[]
    bestellungSumme=0
    dekoPreis=0.00
# Begrüßung
    print("Willkommen! Stellen Sie sich hier ihre Bestellung zusammen. Jede Kugel kostet 75 Cent.")
# Auswahl Waffel/Becher
    while auswahlBecher==False:
        # Bildschirm löschen auskommentieren, wenn weiterführende Zeilen nicht angezeigt werden
        os.system('cls' if os.name == 'nt' else 'clear')
        eingabe=""
        print("Bitte Becher oder Waffel wählen.")
        print("1 - Becher")
        print("2 - Waffel")
        eingabe=input("Drücken Sie 1 für Becher oder 2 für Waffel.")
       
        if eingabe.isnumeric() and int(eingabe)>0 and int(eingabe)<3:
            print("Danke für die Auswahl - weiter zu den Sorten.")
            WaffelBecher=int(eingabe)
            auswahlBecher=True
        else:
            continue
   # sleep(2)
# Auswahl (5x max, 5 Sorten)
    while auswahlEissorten==False and len(bestellung)<KugelMax:
        os.system('cls' if os.name == 'nt' else 'clear')
        eingabe=""
        zaehler=0
        for Sorte in Eissorten:
            zaehler+=1
            print(zaehler," - ",Sorte)
        print("9 - Bestellung abschließen")
        print("0 - Abbruch")
        eingabe=input("Wählen Sie 1-5 Eissorten aus.")
        if eingabe.isnumeric() and int(eingabe)>-1 and int(eingabe)<10:
            if int(eingabe)==0:
                exit()
            if int(eingabe)==9:
                break
            if int(eingabe)>5:
                continue
            bestellung.append(int(eingabe))
            # Alternative, wenn nicht bereits in While-Schleife:
            # if len(bestellung)>KugelMax-1:
            #     break
        else:
            continue
 
    print("Möchten Sie etwas Deko haben? (0 für nein, 1 für ja)")
    for deko in EisDeko:
        eingabetext=deko["artikel"]+ "("+str(deko["preis"])+" €)"
        eingabe=input(eingabetext)
        if eingabe=="1":
           bestellungDeko.append(deko["artikel"])
        dekoPreis+=deko["preis"]*int(eingabe)
       
 
 
# Bestellung (Listenabruf*0.75€)
    endpreis=berechnung()+dekoPreis
# Verabschiedung
    print(bestellungDeko)
 
    verabschieden()
    print("Der Betrag enthielt ", str(round(berechneMWST(endpreis),2)), "an Steuern")
 
 