﻿#arv=input('Arv')


#try:
#    arv=int(arv)
#    print('Int')
#except:
#    try:
#        arv=float(arv)
#        print('float')
#    except:
#        print('Tekst')

#from math import*
#print("Tere! Olen sinu uus sõber - Python!")
#nimi=input('Sinu nimi on ')
#print(nimi,',oi kui ilus nimi!')
#print(nimi,"! Kas leian Sinu keha indeksi? 0-ei, 1-jah")
#g=int(input(''))
#if g==1:
#    try:
#        Pikkus=int(input('Sisestage sinu pikkus => '))
#    except:
#        Pikkus=180
#        print('Error')
#    try:
#        mass=float(input('Sisestage sinu mass => '))
#    except:
#        mass=60
#        print('Error')
#    indeks=round(mass/(0.01*Pikkus)**2, 1)
#    print(nimi,"! Sinu keha indeks on:",indeks)
#    if indeks<16 and indeks>=0:
#        print('Tervisele ohtlik alakaal')
#    elif indeks>=16 and indeks<19:
#        print('Alakaal')
#    elif indeks>=19 and indeks<25:
#        print('Normaalkaal')
#    elif indeks>=25 and indeks<30:
#        print('Ülekaal')
#    elif indeks>=30 and indeks<35:
#        print('Rasvumine')
#    elif indeks>=35 and indeks<40:
#        print('Tugev rasvumine')
#    elif indeks>40:
#        print('Tervisele ohtlik rasvumine')      
#else:
#    print("Kahju! See on väga kasulik info!")
#    print()
#print("Kohtumiseni, "+nimi+"! Igavesti Sinu, Python!")


#from math import*
#print("Tere! Olen sinu uus sõber - Python!")
#nimi=input('Sinu nimi on ')
#print(nimi,',oi kui ilus nimi!')
#print(nimi,"! Kas leian Sinu keha indeksi? 0-ei, 1-jah")
#g=int(input(''))
#if g==1:

#        while True:

#            try:
#                Pikkus=int(input('Sisestage sinu pikkus => '))
#                if Pikkus>0 and Pikkus<273: break
#            except:
#                print('Error')
#        mass=-1
#        while mass<0 or mass>400:
#            try:
#                mass=int(input('Sisestage sinu mass => '))
#            except:
#                print('Error')

#        indeks=round(mass/(0.01*Pikkus)**2, 1)
#        print(nimi,"! Sinu keha indeks on:",indeks)
#        if indeks<16 and indeks>=0:
#            print('Tervisele ohtlik alakaal')
#        elif indeks>=16 and indeks<19:
#            print('Alakaal')
#        elif indeks>=19 and indeks<25:
#            print('Normaalkaal')
#        elif indeks>=25 and indeks<30:
#            print('Ülekaal')
#        elif indeks>=30 and indeks<35:
#            print('Rasvumine')
#        elif indeks>=35 and indeks<40:
#            print('Tugev rasvumine')
#        elif indeks>40:
#            print('Tervisele ohtlik rasvumine')      
#        else:
#            print("Kahju! See on väga kasulik info!")
#            print()
#            print("Kohtumiseni, "+nimi+"! Igavesti Sinu, Python!")


#from math import*
#j=0
#print('Kirjutage 15 numbrid')
#for i in range(1,16,1): #range(15)
#    A=float(input(f'{i} Sisesta A : '))
#    if int(A)==A:  j+=1
#print(j)

#j=0
#i=0
#while True:
#    i+=1
#    A=float(input(f'{i} Sisesta A : '))
#    if int(A)==A: j+=1
#    if i==15: break
#print(j)

j=0
i=0
while i>=0 and i<16:
    i+=1
    A=float(input(f'{i} Sisesta A : '))
    if int(A)==A: j+=1
    if i==15: break
print(j)


print('Sisesta number')
