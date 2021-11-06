def LudzieWSzafkach():
    import shelve
    plik = shelve.open(r'Files\dane_ludzie.dat')
    plik['Adam'] = ['Adam','Małsz',68033154914]
    plik['Kaziu'] = ['Bartosz','Kunicki',72010866459]
    plik['Nikodem'] = ['Kuba','Kowalski',51022591296]

    plik.sync()
    plik.close()
    # odczyt z plikow shelve
    p = shelve.open(r'Files\dane_ludzie.dat')
    print(f"Człek{p['Adam']}")
    print(f"Człek{p['Kaziu']}")
    print(f"Człek{p['Nikodem']}")