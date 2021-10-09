def Pole(r):
    wynik = 3.14*(r**2)
    return wynik

def Obwod(r):
    wynik = 2*3.14*r
    return wynik

#dla maniakow - dodac funkcje obliczajac pole walca, dodac funkcję obliczającą objętość walac
#tip do listy funkcji biblioteki figury dodac funkcję pole prostokata

def PoleProstokata(a,h):
    wynik=a*h
    return wynik

def PoleWalca(r,h):
    a=Obwod(r)
    podstawy=Pole(r)*2
    toduze=PoleProstokata(a,h)
    wynik=podstawy+toduze
    return wynik

def ObjetoscWalca(r,h):
    pk=Pole(r)
    wynik=pk*h
    return wynik