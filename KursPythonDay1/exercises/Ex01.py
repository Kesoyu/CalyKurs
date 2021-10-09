#napisac wfunkcję ktora przetwarza dane z listy peseli wypisuj
#indormacje o płci
def TestowanieKilkuPeseli():
    from libs.tools.PersonalAnalysing import GenderFromPesel
    pesele={'67050796161', '91101193663', '87020364679', '73051462792', '9006O642447', '560713819I7'}
    for x in pesele:
        print(f"Osoba o peselu {x} to {GenderFromPesel(x)}")