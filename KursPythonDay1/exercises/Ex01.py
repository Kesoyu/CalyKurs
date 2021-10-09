#napisac wfunkcję ktora przetwarza dane z listy peseli wypisuj
#indormacje o płci
def TestowanieKilkuPeseli():
    from libs.tools.PersonalAnalysing import GenderFromPesel
    pesele={'67050796161', '91101193663', '87020364679', '73051462792', '9006O642447', '560713819I7'}
    for x in pesele:
        print(f"Osoba o peselu {x} to {GenderFromPesel(x)}")

#dodac do tools do mathmath funkcję obliczającą polek ola oraz funkcję obliczającą obwód koła
#ww funkcję użyć dla przykładowej listy promieni i obliczyć pola i obwody
# ** potega operator
#import mathmath
#mathmath.pow(promien,2) funkcja potegi

def ObwodyPola():
    from libs.mathmath.kola import Pole, Obwod
    promienie = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    [print(f"Obwod kola o promieniu {x}: {Obwod(x)}\nPole kola o promieniu {x}: {Pole(x)}") for x in promienie]

#dla maniakow - dodac funkcje obliczajac pole walca, dodac funkcję obliczającą objętość walac
#tip do listy funkcji biblioteki figury dodac funkcję pole prostokata

def PoleObjetoscWalca():
    from libs.mathmath.kola import import

