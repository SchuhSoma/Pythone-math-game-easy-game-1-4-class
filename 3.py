import random
nevBe=input("Kérem adja meg a nevét: ")
Nev=nevBe
print("\t1-es gomb ÖSSZEADÁS\n\t2-es gomb KIVONÁS\n\t3-as gomb SZORZÁS\n\t4-es gomb OSZTÁS")
valasztasBe=input("\nKérem válasszon gyakorló témakört: ")
Valasztas=int(valasztasBe)
#------------------------------------------------------------------------------------------------
joValaszokSzama=0
rosszValaszokSzama=0;
#------------------------------------------------------------------------------------------------
if Valasztas==1:
    print(Nev," Ön az összeadást választotta:")
    for i in range(10):
        Aszam=random.randrange(0,100)
        Bszam=random.randrange(0,100)
        Osszeg=Aszam+Bszam
        print("\tMondja meg mennyi a két szám összege: ",Aszam ," + ",Bszam," =")
        felahasznaloValasz=input("\tKérem adja meg az eredményt: ")
        Valasz=int(felahasznaloValasz)
        if Valasz==Osszeg:
            joValaszokSzama+=1
            print("\tHelyes válasz garatulálok")
        else:
            rosszValaszokSzama+=1
            print("\tSajnálom rossz választ adott a helyes eredmény: ",Osszeg)
#---------------------------------------------------------------------------------------
elif Valasztas==2:
    print(Nev," Ön a kivonást választotta:")
    for i in range(10):
        Aszam = random.randrange(0, 100)
        Bszam = random.randrange(0, 100)
        if Aszam<Bszam:
            Kulonbseg=Bszam-Aszam
            print("\tMondja meg mennyi a két szám különbségét: ", Bszam, " - ", Aszam, " =")
            felahasznaloValasz = input("\tKérem adja meg az eredményt: ")
            Valasz = int(felahasznaloValasz)
        else:
            Kulonbseg=Aszam-Bszam
            print("\tMondja meg mennyi a két szám különbségét: ", Aszam, " - ", Bszam, " =")
            felahasznaloValasz = input("\tKérem adja meg az eredményt: ")
            Valasz = int(felahasznaloValasz)
        if Valasz == Kulonbseg:
            joValaszokSzama += 1
            print("\tHelyes válasz garatulálok")
        else:
            rosszValaszokSzama += 1
            print("\tsajnálom rossz választ adott a helyes eredmény: ", Kulonbseg)
#------------------------------------------------------------------------------------------
elif Valasztas==3:
    print(Nev," Ön a szorzást választotta:")
    for i in range(10):
        Aszam = random.randrange(2, 10)
        Bszam = random.randrange(2, 10)
        Szorzat=Aszam*Bszam
        print("\tMondja meg mennyi a két szám szorzatát: ", Bszam, " × ", Aszam, " =")
        felahasznaloValasz = input("\tKérem adja meg az eredményt: ")
        Valasz = int(felahasznaloValasz)
        if Valasz == Szorzat:
            joValaszokSzama += 1
            print("\tHelyes válasz garatulálok")
        else:
            rosszValaszokSzama += 1
            print("\tsajnálom rossz választ adott a helyes eredmény: ", Szorzat)
#------------------------------------------------------------------------------------------
elif Valasztas==4:
    print(Nev," Ön az osztást választotta:")
    for i in range(10):
        Aszam = random.randrange(2, 20)
        Bszam = random.randrange(2, 20)
        Szorzat=Aszam*Bszam
        if Aszam<Bszam:
            print("\tMondja meg mennyi a két szám osztási eredménye: ", Szorzat, " ÷ ", Bszam, " =")
            felahasznaloValasz = input("\tKérem adja meg az eredményt: ")
            Valasz = int(felahasznaloValasz)
        else:
            print("\tMondja meg mennyi a két szám osztási eredményét: ", Szorzat, " ÷ ", Bszam, " =")
            felahasznaloValasz = input("\tKérem adja meg az eredményt: ")
            Valasz = int(felahasznaloValasz)
        if Valasz == Aszam or Valasz==Bszam:
            joValaszokSzama += 1
            print("\tHelyes válasz garatulálok")
        else:
            rosszValaszokSzama += 1
            print("\tsajnálom rossz választ adott a helyes eredmény: ", Aszam)
#------------------------------------------------------------------------------------------
if joValaszokSzama==10:
    print("\n\tGratulálok ",Nev," nagyon ügyes vagy igazi matek zseni :)")
    print("\tHelyes válaszok száma: ",joValaszokSzama)
elif joValaszokSzama==9:
    print("\n\tGratulálok ",Nev," nagyon jó matekos vagy")
    print("\tHelyes válaszok száma: ", joValaszokSzama)
elif joValaszokSzama==8:
    print("\n\tGratulálok ",Nev," jó matekos vagy")
    print("\tHelyes válaszok száma: ", joValaszokSzama)
elif joValaszokSzama==7:
    print("\n\t", Nev, " közepes matekos vagy")
    print("\tHelyes válaszok száma: ", joValaszokSzama)
elif joValaszokSzama==6:
    print("\n\t",Nev," fejlődőképes matekos vagy")
    print("\tHelyes válaszok száma: ", joValaszokSzama)
elif joValaszokSzama<6:
    print("\n\t",Nev," sajnálom neked még gyakorolnod kell")
    print("\tHelyes válaszok száma: ", joValaszokSzama)