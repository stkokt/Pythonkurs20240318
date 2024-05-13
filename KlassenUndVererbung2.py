
class Kuchen():
    
    def __init__(self, eier, zucker, butter, mehl):
        self._eier=eier
        self._zucker=zucker
        self._butter=butter
        self._mehl=mehl

    # Magic Functions

    # Ohne repr mal printen!    
    def __repr__(self):
        return f"Kuchen({self._eier}, {self._zucker}, {self._butter}, {self._mehl})"

    # Mal ohne eq vergleichen!   
    def __eq__(self, other):
        if not isinstance(other, Kuchen):
            return False
        return self._eier==other._eier and \
            self._zucker==other._zucker and \
            self._butter==other._butter and \
            self._mehl==other._mehl
    

    # Mal ohne gt vergleichen!  
    def __gt__(self, other):
        if not isinstance(other, Kuchen):
            return False
        return self._zucker>other._zucker and \
            self._butter>other._butter and \
            self._mehl>other._mehl



kuchen1=Kuchen(3,200,150,200)
kuchen2=Kuchen(3,200,150,200)
kuchen3=Kuchen(5,400,150,300)
kuchen4=Kuchen(3,300,200,300)

print(kuchen1>kuchen2)


class Party:
    def __init__(self, size):
        self._kuchen = []
        self._size = size

    def add_kuchen(self, kuchen):
        if not isinstance(kuchen, Kuchen):
            raise TypeError("Nur Kuchen mitbringen!")
        if len(self._kuchen) >= self._size:
            raise ValueError("So viele Kuchen kann doch keiner essen!")
        self._kuchen.append(kuchen)

    # geburtstagsparty+=kuchen geht ohne __add__ nicht
    def __add__(self, other):
        if not isinstance(other, Kuchen):
            raise TypeError("Nur Kuchen mitbringen!")
        new_party=Party(self._size)
        for kuchen in self._kuchen:
            new_party.add_kuchen(kuchen)
        new_party.add_kuchen(other)
        return new_party
    
    # kuchen+=geburtstagsparty geht ohne __add__ nicht
    def __radd__(self, other):
        return self+other
    
    # Beide folgende Funktionen machen das Iterireren über 
    # self._kuchen möglich in der Form
    # for kuchen in geburtstagsparty:
    # print(kuchen)
    def __iter__(self):
        return iter(self._kuchen)
    
    def __next__(self):
        if self.index > len(self._kuchen):
            raise StopIteration
        new_kuchen =next(self)
        self.index+=1
        return new_kuchen


geburtstagsparty= Party(3)

geburtstagsparty.add_kuchen(kuchen1)
geburtstagsparty.add_kuchen(kuchen2)
#geburtstagsparty.add_kuchen(kuchen3)
kuchen4+=geburtstagsparty

for kuchen in geburtstagsparty:
    print(kuchen)
