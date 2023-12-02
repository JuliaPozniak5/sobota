''' JP   '''


'''Zadanie 1 
Napisz program umożliwiający obliczenie ile paliwa spala samochód na 100 km.
Dane wczytane to zużyte paliwo 22 litry i przejechana trasa 600 km. '''

'''
paliwo=22
trasa=600
spalanie=100

print(paliwo * trasa / spalanie)'''

'''
paliwo = int(input("zużyte paliwo: "))
trasa = int(input("przejechane kilometry: "))
spalanie=100
print("spalanie",round( paliwo *spalanie / trasa,2))
'''




'''
Zadanie 2
Mając daną wartość a=2 zwiększ jej wartośc o 10, następnie zmiejsz o 3.
Podnieś do potęgi drugiej a na koniec podziel przez 3. Wyświetl każdy z etapów.'''

'''
a=2
b=a+10
c=b-3
d=c**2
e=d-3

print(a,b,c,d,e)
'''





'''
Zadanie 3
Napisz program wczytujący wartość a z klawiatury. Program zwraca informację a<0, a=0, a>0'''

'''
def x(a):
    if a==0:
        print("a=0")
    elif a>0:
        print("a>0")
    else:
        print ("a<0")

a = int(input("podaj liczbę: "))
x(a)
'''





'''
Zadanie 4
Napisz program z użyciem for liczący od 1 do wartości podanej z klawiatury.'''

'''
a = int(input("podaj liczbę: "))

for i in range(1,a+1):
    print("warotści:", i)

'''




'''
Zadanie 5
Napisz program z użyciem pętli while liczący od 1 do wartości podanej z klawiatury. '''

'''
a = int(input("podaj liczbę : "))
i=1
while i<a+1:
    print(i)
    i+=1
 '''   






'''
Zadanie 6
Napisz program z wykorzystaniem dowolnej pętli sumujący 3 liczby wczytane z klawiatury'''


'''
a = int(input("podaj liczbę a: "))
b = int(input("podaj liczbę b: "))
c = int(input("podaj liczbę c: "))

for i in range(a,b,c):
    print("suma", a+b+c)

'''





'''
Zadanie 7
Napisz program liczący od 1 do 10 i pomijający wyświetlenie cyfry 6 '''

'''

i=1
while i<11: #pęetla w górę
    print(i)
    i+=1 and i!=6

'''

'''
Zadanie 8
Napisz program z użyciem for liczący od 10 do 1 co 1
'''

'''
for i in range(10,0,-1):
    print(i)
'''





'''
Zadanie 9 Mając listę o nazwie samochod=['audi','fiat',citroen','peugeot'] wykonaj:
b)skasuj element 2 listy
a)pokaż element 1 listy
'''

'''
samochod=['audi','fiat','citroen','peugeot']

samochod.pop(1)
print(samochod)

print(samochod[0])
'''






'''
Zadanie 10
Mając krotkę o nazwie samochod=('audi','fiat',citroen','peugeot') wykonaj:
a) pokaz ostatni element krotki'''

'''
samochod=('audi','fiat','citroen','peugeot')
print([samochod[-1]])

'''


'''
Zadanie 11 
napisz program,który oblicza pole i obwód koła o promieniu podanym przez użytkownika.
Wartość stałej pi weź z biblioteki math. Promień nie może być ujemny. W przypadku podania liczby ujemnej,
program powinien wypisywać komunikat informujący o błędnej wartości i nic nie liczyć.'''


'''
if pole<=0:
    print("Blędna wartość promienia")
    else:
        print(pole)
'''
'''
import math
r = int(input("podaj promien koła r: "))
pi=math.pi
#pole = pi * r ** 2
obwod=2*pi*r

pole = ((math.pow(r,2)) * pi)
#print(pole)

pole_kola=f'Pole koła = {pole:.2f} cm2'

if r<=0:
    print("Blędna wartość promienia")
else:
        print(pole_kola)
        print("Obwód koła",round(obwod,2))
'''
