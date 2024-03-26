from time import sleep
import os
import EisdieleFunk


while True:

# Begrüßung
    print("Willkommen! Stellen Sie sich hier ihre Bestellung zusammen. Jede Kugel kostet 75 Cent.")
# Auswahl Waffel/Becher
    while EisdieleFunk.auswahlBecher==False:
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
            EisdieleFunk.auswahlBecher=True
        else:
            continue
   # sleep(2)
# Auswahl (5x max, 5 Sorten)
    while EisdieleFunk.auswahlEissorten==False and len(EisdieleFunk.bestellung)<EisdieleFunk.KugelMax:
        os.system('cls' if os.name == 'nt' else 'clear')
        eingabe=""
        zaehler=0
        for Sorte in EisdieleFunk.Eissorten:
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
            EisdieleFunk.bestellung.append(int(eingabe))
            # Alternative, wenn nicht bereits in While-Schleife:
            # if len(bestellung)>KugelMax-1:
            #     break
        else:
            continue
 
    print("Möchten Sie etwas Deko haben? (0 für nein, 1 für ja)")
    for deko in EisdieleFunk.EisDeko:
        eingabetext=deko["artikel"]+ "("+str(deko["preis"])+" €)"
        eingabe=input(eingabetext)
        if eingabe=="1":
           EisdieleFunk.bestellungDeko.append(deko["artikel"])
        EisdieleFunk.dekoPreis+=deko["preis"]*int(eingabe)
       
 
 
# Bestellung (Listenabruf*0.75€)
    EisdieleFunk.endpreis=EisdieleFunk.berechnung()+EisdieleFunk.dekoPreis
# Verabschiedung
    print(EisdieleFunk.bestellungDeko)
 
    EisdieleFunk.verabschieden()
    print("Der Betrag enthielt ", str(round(EisdieleFunk.berechneMWST(EisdieleFunk.endpreis),2)), "an Steuern")
 
 