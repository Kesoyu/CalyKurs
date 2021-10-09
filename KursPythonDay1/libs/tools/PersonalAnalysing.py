def GenderFromPesel(pesel):
    if len(pesel)==11 and pesel.isnumeric():#jezeli wszystkie wartosci pesela sa cyframi
        gender = int(pesel[9])
        return "dziewczynka" if gender % 2 == 0 else "chlopczyk"
    else:
        return "zle podany pesel"