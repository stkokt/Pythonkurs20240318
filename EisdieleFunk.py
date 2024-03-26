WaffelBecher=0
KugelMax=5
KugelPreis=0.75
Eissorten=("Erdbeer","Zitrone","Joghurt","Vanille","Schoko")
EisDeko=({"artikel":"Sahne ", "preis":0.50}, {"artikel":"Streusel", "preis":0.20})
 
auswahlBecher=False
auswahlEissorten=False
bestellung=[]
bestellungDeko=[]
bestellungSumme=0
dekoPreis=0.00

endpreis=float()


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
