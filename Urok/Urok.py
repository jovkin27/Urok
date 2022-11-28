#arv=input('Arv')


#try:
#    arv=int(arv)
#    print('Int')
#except:
#    try:
#        arv=float(arv)
#        print('float')
#    except:
#        print('Tekst')

from math import*
print("Tere! Olen sinu uus sõber - Python!")
nimi=input('Sinu nimi on ')
print(nimi,',oi kui ilus nimi!')
print(nimi,"! Kas leian Sinu keha indeksi? 0-ei, 1-jah")
g=int(input(''))
if g==1:
    try:
        Pikkus=int(input('Sisestage sinu pikkus => '))
    except:
        Pikkus=180
        print('Error')
    try:
        mass=float(input('Sisestage sinu mass => '))
    except:
        mass=60
        print('Error')
    indeks=round(mass/(0.01*Pikkus)**2, 1)
    print(nimi,"! Sinu keha indeks on:",indeks)
    if indeks<16 and indeks>=0:
        print('Tervisele ohtlik alakaal')
    elif indeks>=16 and indeks<19:
        print('Alakaal')
    elif indeks>=19 and indeks<25:
        print('Normaalkaal')
    elif indeks>=25 and indeks<30:
        print('Ülekaal')
    elif indeks>=30 and indeks<35:
        print('Rasvumine')
    elif indeks>=35 and indeks<40:
        print('Tugev rasvumine')
    elif indeks>40:
        print('Tervisele ohtlik rasvumine')      
else:
    print("Kahju! See on väga kasulik info!")
    print()
print("Kohtumiseni, "+nimi+"! Igavesti Sinu, Python!")