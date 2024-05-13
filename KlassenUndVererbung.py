#################### Falsche Implementierung #################################

""" class Kuchen:

    
        sorte=""
        eier=3
        mehl=200
        butter=150
        geruehrt=False
        gebacken=False

        def ruehren():
            print(f"Teig fuer {sorte} wird geruehrt.")
            geruehrt=True

        def backen():
            if geruehrt == True:
                print(f"{sorte} wird gebacken")
                gebacken = True
            else:
                print(f"{sorte} muss erst geruehrt werden")

        def essen(self):
            if gebacken == True:
                print(f"{sorte} wird gegessen")
            else:
                print(f"{sorte} muss erst gebacken werden")


kuchen1 = Kuchen()
kuchen2 = Kuchen()

kuchen1.ruehren(kuchen1)
kuchen1.backen()
kuchen1.essen()

kuchen2.ruehren()
kuchen2.backen()
kuchen2.essen()

 """

#################### Ende Falsche Implementierung ###############################

#################### Richtige Implementierung ###################################

""" class Kuchen:

    def __init__(self, sorte, eier, mehl, butter):
        self.sorte=sorte
        self.eier=eier
        self.mehl=mehl
        self.butter=butter
        self.geruehrt=False
        self.gebacken=False

    def ruehren(self):
        print(f"Teig fuer {self.sorte} wird geruehrt.")
        self.geruehrt=True

    def backen(self):
        if self.geruehrt == True:
            print(f"{self.sorte} wird gebacken")
            self.gebacken = True
        else:
            print(f"{self.sorte} muss erst geruehrt werden")

    def essen(self):
        if self.gebacken == True:
            print(f"{self.sorte} wird gegessen")
        else:
            print(f"{self.sorte} muss erst gebacken werden")


kuchen1 = Kuchen('Kirschkuchen', 3, 200, 150)
kuchen2 = Kuchen('Kaesekuchen', 5, 150, 50)

kuchen1.ruehren()
kuchen1.backen()
kuchen1.essen()

kuchen2.ruehren()
kuchen2.backen()
kuchen2.essen() """

#################### Ende Richtige Implementierung ##############################

################################ Vererbung ######################################

class Kuchen:

    def __init__(self, form):
        self.form=form
        self.geruehrt=False
        self.gebacken=False

    def ruehren(self):
        print(f"Teig fuer {self.sorte} wird geruehrt.")
        self.geruehrt=True

    def backen(self):
        if self.geruehrt == True:
            print(f"{self.sorte} wird gebacken")
            self.gebacken = True
        else:
            print(f"{self.sorte} muss erst geruehrt werden")

    def essen(self):
        if self.gebacken == True:
            print(f"{self.sorte} wird gegessen")
        else:
            print(f"{self.sorte} muss erst gebacken werden")


#class Kirschkuchen(Kuchen):

# Implementierung mit eigenen Übergabeparametern für die Kindklasse

"""     def __init__(self, form, eier, mehl, butter):
        super().__init__(form)

        self.sorte="Kirschkuchen"
        self.eier=eier
        self.mehl=mehl
        self.butter=butter """

# Implementierung mit spezifischen Feldern und überschriebenen Methoden

class Kirschkuchen(Kuchen):
    def __init__(self, form):
        super().__init__(form)

        self.sorte="Kirschkuchen"
        self.spezielleZutat="Kirschen"
        self.eier=2
        self.mehl=200
        self.butter=150

    def ruehren(self):
        print(f"{self.eier} Eier, {self.mehl}gr Mehl und {self.butter}gr Butter fuer {self.sorte} wird geruehrt.")
        self.geruehrt=True

    def backen(self):
        print(f"Teig wird in {self.form} gegeben.")
        print(f"{self.spezielleZutat} kommen oben drauf.")
        super().backen()
        

kuchen1=Kirschkuchen('Springform')

kuchen1.ruehren()
kuchen1.backen()
kuchen1.essen()
print(kuchen1.eier)

############################# Ende Vererbung ####################################

########################## Mehrfach- Vererbung ##################################

class Haus:

    def __init__(self, laenge, breite, hoehe, etagen):
        self.laenge=laenge
        self.breite=breite
        self.hoehe=hoehe
        self.etagen=etagen
        self.dachboden=True
        self.keller=True

        self.baujahr=1980

    def bauen(self):
        print(f"{type(self)} wird gebaut")


haus1= Haus(10, 10, 10, 2)
#haus1.bauen()


class Fahrzeug:

    def __init__(self, raeder, sitze, kmh):

        self.raeder=raeder
        self.sitze=sitze
        self.kmh=kmh

        self.baujahr=2020

    def fahren(self):
        print(f"BrummBrumm mit {self.kmh} km/h")


class Wohnmobil(Haus, Fahrzeug):

    def __init__(self, laenge, breite, hoehe, etagen, raeder, sitze, kmh):
        super().__init__(laenge, breite, hoehe, etagen) and super().__init__(raeder, sitze, kmh)
        self.laenge=laenge
        self.breite=breite
        self.hoehe=hoehe
        self.etagen=etagen
        self.dachboden=False
        self.keller=False
        self.raeder=raeder
        self.sitze=sitze
        self.kmh=kmh


    def fahren(self):
        print(f"ToeffToeff mit {self.kmh} km/h")

camper = Wohnmobil(10, 5, 2, 1, 4, 2, 80 )

camper.bauen()
camper.fahren()

print(camper.breite)
#print(camper.baujahr)
    