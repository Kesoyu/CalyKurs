def Pliki():
    while(True):
        odp = input("Zapis do pliku txt danych podanych w konsoli\n1 - podaj dane do zapisu\n2-odczytaj dane z txt\n3 - zapis danych do CSV\n4 - odczyt danych CSV\nK-koniec\n")
        if odp=="1":
            dane = input("Podaj dane do zapisu w pliku\n")
            plik = open(r'Files/dane_osobowe.txt','a',encoding="UTF-8")
            plik.write(dane+"\n")
            plik.close()
        elif odp=="2":
            with open(r'Files/dane_osobowe.txt','r',encoding="UTF-8") as plik:
                for l in plik:
                    print(l.rstrip("\n"))
        elif odp=="3":
            import os
            # print(os.__doc__)
            if os.path.exists(os.getcwd()+r'\Files/dane_firmowe'):
                pass
            else:
                os.mkdir(os.getcwd() + r'\Files/dane_firmowe')

            imie = input("Podaj imie\n")
            nazwisko = input("Podaj nazwisko\n")
            pesel = input("Podaj pesel\n")
            with open(r'Files\dane_firmowe\osoby.csv', 'a', encoding="UTF-8") as plik:
                print(imie, nazwisko, pesel, sep=":", file=plik)

            import csv
            with open(r'Files\dane_firmowe\osoby_lib_csv.csv', 'a', encoding="UTF-8") as plik_csv:
                zapis_csv =csv.writer(plik_csv, delimiter=",")
                zapis_csv.writerow([imie, nazwisko, pesel])
        elif odp=="4":
            from libs.tools.PersonalAnalysing import GenderFromPesel, DateFromPesel
            import os, csv
            if os.path.exists(os.getcwd()+r'\Files/dane_firmowe/osoby.csv'):
                print("test")
                with open(r'Files/dane_firmowe/osoby.csv', 'r', encoding="UTF-8") as plik:
                    for l in plik:
                        dane = l.split(":")
                        pesel = dane[2].rstrip('\n')
                        print(pesel)
                        print(f"{dane[0]} {dane[1]} to {GenderFromPesel(pesel)}")
                        print(f"{'urodzona' if GenderFromPesel(pesel) == 'dziewczynka' else 'urodzony'}")
                        print(f"{DateFromPesel(pesel)}")
            if os.path.exists(os.getcwd()+r'\Files/dane_firmowe/osoby_lib_csv.csv'):
                print("test")
                with open(r'Files/dane_firmowe/osoby_lib_csv.csv', 'r', encoding="UTF-8") as plik:
                    csv_reader = csv.reader(plik, delimiter=',')

                    for dane in csv_reader:
                        if(len(dane)) > 0:
                            try:
                                pesel = dane[2].rstrip('\n')
                                print(f"{dane[0]} {dane[1]} to {GenderFromPesel(pesel)}")
                                print(f"{'urodzona' if GenderFromPesel(pesel) == 'dziewczynka' else 'urodzony'}")
                                print(f"{DateFromPesel(pesel)}")
                            except Exception as e:
                                print(e)
            import sys
            print("do widzenia")
            sys.exit()