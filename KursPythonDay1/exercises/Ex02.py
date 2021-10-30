def Test_RozpoczecieDnia():
    while True:
        from libs.tools.Testy import TestNumber
        print("Co chesz robic")
        print("1[Policz funkcje kwadratowa]")
        print("2[Policz 2 niewiadome]")
        print("K[Wyjdz]")
        odp=input()
        if odp=="1":
            from libs.mathmath.kola import FunkcjaKwadratowa
            a=input()
            b=input()
            c=input()
            TestNumber(a)
            TestNumber(b)
            TestNumber(c)
            if TestNumber(a) and TestNumber(b) and TestNumber(c):
                a = float(a)
                b = float(b)
                c = float(c)
                try:
                        x, y = FunkcjaKwadratowa(a, b, c)
                        print(f"x1={x:.2f}\nx2={y:.2f}")
                except Exception as e:
                    print(e)
            else:
                print("Wszystkie podane dane nie sa liczbą")
        elif odp=="2":
            from libs.mathmath.kola import MetodaWyznacznikow
            a = input()
            b = input()
            c = input()
            d = input()
            e = input()
            f = input()
            TestNumber(a)
            TestNumber(b)
            TestNumber(c)
            TestNumber(d)
            TestNumber(e)
            TestNumber(f)
            if TestNumber(a) and TestNumber(b) and TestNumber(c):
                a = float(a)
                b = float(b)
                c = float(c)
                d = float(d)
                e = float(e)
                f = float(f)
                try:
                    x, y = MetodaWyznacznikow(a, b, c, d, e, f)
                    print(f"x1={x:.2f}\nx2={y:.2f}")
                except Exception as e:
                    print(e)
            else:
                print("Wszystkie podane dane nie sa liczbą")
        else:
            print("Do zobaczenie")
            import sys
            sys.exit()